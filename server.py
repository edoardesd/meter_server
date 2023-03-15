import json
import re
import signal
import socket
import sys
import paho.mqtt.client as mqtt

BROKER_ADDRESS = "test.mosquitto.org"
TOPIC_TO_PUBLISH = "polimi/fiorentini/meter"
localIP = "131.175.120.22"
localPort = 8883
bufferSize = 1024
msg_counter = 0
_json = {"regular": [0, 0], "forward": [0, 0], "last_event": "test"}
sender_ids = dict()
debug = False

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


def on_message(_, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


def on_connect(_client, _, flags, rc):
    print("Connected with result_code " + str(rc))


def parse_string(msg):
    msg_content = msg.decode().split("A")
    try:
        msg_id = int(msg_content[1])
        msg_rsrq = int(msg_content[2])
    except ValueError as e:
        print("someone is not an integer: {}  {} - err: {}".format(e, msg_content[1], msg_content[2]))
    return msg_content[0], msg_id, msg_rsrq


def parse_meter_id(mtr_id):
    mtr_id = re.sub("[^0-9]", "", mtr_id)
    try:
        mtr_id = int(mtr_id)
    except ValueError as e:
        print("meter id is not an integer: {} - err: {}".format(e, mtr_id,))
    return mtr_id


def update_stats(fwd, _id):
    if fwd:
        _json["forward"][abs(_id-1)] += 1
    else:
        _json["regular"][_id] += 1


def check_forward(_id):
    if _id.startswith('f'):
        return True, _id
    else:
        return False, _id


def signal_handler(sig, frame):
    print('Store & Exit, CTRL+C pressed')
    sys.exit()


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
    meter_id, message_id, message_rsrq = parse_string(message)
    forward, meter_id = check_forward(meter_id)

    update_stats(forward, parse_meter_id(meter_id))

    print(json.dumps(_json))
    client.publish(TOPIC_TO_PUBLISH, json.dumps(_json), retain=True)

    if debug:
        clientMsg = "Message from Client:{}".format(message)
        print(meter_id, message_id, message_rsrq)
        print(sender_ids)
        print(clientMsg)
