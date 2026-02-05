"""
Simple MQTT Subscriber - waits for one message and exits.

Uses the high-level paho.mqtt.subscribe API for one-shot receiving.
"""

import paho.mqtt.subscribe as subscribe

print("Waiting for message on topic 'ee250'...")

# subscribe.simple() connects, waits for one message, then disconnects
# This call blocks until a message arrives on the specified topic
m = subscribe.simple("ee250", hostname="test.mosquitto.org")

# Print the topic and decoded message payload
print((m.topic, m.payload.decode()))
