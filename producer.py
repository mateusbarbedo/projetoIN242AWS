import paho.mqtt.client as mqtt
import json

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.224.138.100', 1883)

print(' Qantidade de pessoas')
pessoas = int(input('Entre com o num de pessoas: '))
print('\a')
print(pessoas)

mensagem = {
    'Portaria': 'total',
    'pessoas': pessoas
}

mqtt_client.publish('in242', json.dumps(mensagem))
