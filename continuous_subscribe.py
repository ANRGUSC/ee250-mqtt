"""
Continuous MQTT Subscriber - listens for messages indefinitely.

Uses the callback-based MQTT client for long-running subscriptions.
Unlike subscribe.py, this keeps running until you press Ctrl+C.
"""

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

# Configuration
TOPIC = "ee250"
BROKER = "test.mosquitto.org"


def on_connect(client, userdata, flags, rc):
    """Called when the client connects to the broker."""
    if rc == 0:
        print(f"Connected to {BROKER}")
        client.subscribe(TOPIC)
        print(f"Subscribed to '{TOPIC}'. Waiting for messages... (Ctrl+C to exit)")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    """Called when a message is received on a subscribed topic."""
    print(f"({msg.topic}, {msg.payload.decode()})")


# Create client with explicit API version (required for paho-mqtt 2.0+)
client = mqtt.Client(CallbackAPIVersion.VERSION1)

# Attach callback functions to handle events
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker: hostname, port, keepalive interval (seconds)
client.connect(BROKER, 1883, 60)

# Run the network loop forever, processing callbacks
# This blocks until client.disconnect() is called or an error occurs
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnecting...")
    client.disconnect()
