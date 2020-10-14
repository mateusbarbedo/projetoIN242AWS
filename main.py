version: "3.5"
services:
  mqtt-broker:
    hostname: mqtt-broker
    image: eclipse-mosquitto
    ports:
      - "1883:1883"
  mongo-db:
    hostname: mongo-db
    image: mongo
    ports:
      - "27018:27017"
