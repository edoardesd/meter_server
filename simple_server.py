import signal
import socket
import sys

localIP = "131.175.120.22"
localPort = 8883
bufferSize = 1024
msg_counter = 0

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


def signal_handler(sig, frame):
    print('Store & Exit, CTRL+C pressed')
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)

print("UDP server up and listening")


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    msg_counter += msg_counter
    message = bytesAddressPair[0]
    address_port = bytesAddressPair[1]

    print(message, address_port)
