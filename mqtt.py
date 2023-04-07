import paho.mqtt.client as mqtt
broker_address="test.mosquitto.org"

print("creating new instance")

client = mqtt.Client("mqtt-client-polimi-smart-meter") #create new instance
print("connecting to broker")
client.connect(broker_address)
print("Publishing message to topic")
_json = {"meter0": [999, 10], "meter1": [2, 83]}
client.publish("polimi/fiorentini/meter", str(_json))

