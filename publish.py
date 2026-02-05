"""
Simple MQTT Publisher - sends a single message and exits.

Uses the high-level paho.mqtt.publish API for one-shot publishing.
"""

import paho.mqtt.publish as publish

# publish.single() connects, sends one message, and disconnects automatically
# Arguments: topic, message payload, broker hostname
publish.single("ee250", "Hello EE 250 folks", hostname="test.mosquitto.org")
print("Message published!")
