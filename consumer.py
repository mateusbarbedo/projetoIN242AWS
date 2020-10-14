import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import datetime

mongo_client = MongoClient('18.224.138.100',27017)
mongo_db = mongo_client['in242']
mongo_collection = mongo_db['pessoas']

def msg_recebida(mqtt_client,obj, msg):
    print('Recebendo mensagem...')
    print(msg.payload)
    msg_formatada = json.loads(msg.payload)
    msg_formatada['data da coleta'] = datetime.datetime.now()
    mongo_collection.insert_one(msg_formatada)
    print('Mensagem inserida...')

print('Conectando ao broker MQTT...')

mqtt_client = mqtt.Client()
mqtt_client.connect('mqtt-broker', 1883)
mqtt_client.on_message = msg_recebida
mqtt_client.subscribe('in242')
mqtt_client.loop_forever()