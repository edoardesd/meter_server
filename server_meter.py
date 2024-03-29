import json
import re
import signal
import socket
import sys
import paho.mqtt.client as mqtt

import parser
import argparse

BROKER_ADDRESS ="91.121.93.94" #"test.mosquitto.org"
TOPIC_TO_PUBLISH = "polimi/fiorentini/meter_1"
localIP = "131.175.120.22"
localPort = 8883
bufferSize = 1024
msg_counter = 0
_json = {"regular": [0, 0], "forward": [0, 0], "last_event": "Welcome"}
sender_ids = dict()
debug = True



# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.close()

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


def on_message(_, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


def on_connect(_client, _, flags, rc):
    print("Connected with result_code " + str(rc))


def signal_handler(sig, frame):
    print('Store & Exit, CTRL+C pressed')
    sys.exit()


pars = argparse.ArgumentParser(description='Example program to demonstrate fiorentini ble meter')

pars.add_argument('-s', '--shortrange', type=str, default='C', help='Meter short range')

args = pars.parse_args()

signal.signal(signal.SIGINT, signal_handler)

print("UDP server up and listening")
print("creating new MQTT instance")

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.connect(BROKER_ADDRESS)
client.publish(TOPIC_TO_PUBLISH, json.dumps(_json), retain=True)

client.loop_start()

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    msg_counter += msg_counter
    message = bytesAddressPair[0]
    address_port = bytesAddressPair[1]
    if debug: print("Message received {}".format(message))

    generator_id, forwarder_id = parser.parse_message(message.decode("utf-8"))
    _json = parser.update_stats(generator_id, forwarder_id, _json, args.shortrange)

    print(json.dumps(_json))
    client.publish(TOPIC_TO_PUBLISH, json.dumps(_json), retain=True)

    if debug:
        clientMsg = "Message content: {}".format(message)
        print(generator_id)
        print(forwarder_id)
