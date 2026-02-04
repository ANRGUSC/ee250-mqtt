import paho.mqtt.subscribe as subscribe

print("Waiting for message on topic 'ee250'...")
m = subscribe.simple('ee250', hostname="test.mosquitto.org")
print((m.topic, m.payload))
