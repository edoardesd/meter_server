# How to run it: uvicorn api:app --reload

from fastapi import FastAPI
import ast
import paho.mqtt.client as mqtt
from starlette.middleware.cors import CORSMiddleware

BROKER_ADDRESS = "test.mosquitto.org"
TOPIC_TO_SUBSCRIBE = "polimi/fiorentini/meter"
app = FastAPI()
global msg_forward
msg_forward = {"m0": [0, 0], "m1": [0, 0], "last_event": "test"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/meter_status")
def api_call():
    global msg_forward
    return msg_forward


def on_message(_, userdata, message):
    global msg_forward
    msg_forward = str(message.payload.decode('utf8'))
    msg_forward = ast.literal_eval(msg_forward)
    print("message received ", msg_forward)


def on_connect(_client, _, flags, rc):
    print("Connected flags" + str(flags) + "result_code" + str(rc) + str(_client))


print("creating new MQTT instance")
client = mqtt.Client("mqtt-client-polimi-smart-meter-server")
client.on_message = on_message
client.on_connect = on_connect
client.connect(BROKER_ADDRESS)
client.subscribe(TOPIC_TO_SUBSCRIBE)

client.loop_start()




