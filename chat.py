"""
MQTT Chat - A simple pub/sub chat application

- SUBSCRIBE to a topic to receive messages from others
- PUBLISH to the same topic to send messages
- Threading lets us receive messages while waiting for user input
"""

import paho.mqtt.client as mqtt
import threading
import random

# Configuration
TOPIC = "ee250"
BROKER = "test.mosquitto.org"
INDENT = " " * 40  # Our messages appear indented to distinguish from others
MY_ID = f"{random.randint(0, 9999):04d}"  # Random 4-digit ID for this session

# Used to filter out our own messages when they echo back
my_last_message = None


def on_connect(client, userdata, flags, rc):
    """Called automatically when we connect to the broker."""
    print(f"Connected to {BROKER} (your ID: {MY_ID})")
    client.subscribe(TOPIC)
    print(f"Joined '{TOPIC}'. Type messages and press Enter.")
    print(INDENT, end="", flush=True)


def on_message(client, userdata, msg):
    """Called automatically when a message arrives."""
    global my_last_message
    text = msg.payload.decode()

    # Don't display our own message (we already see it as we type)
    if text == my_last_message:
        my_last_message = None
        return

    # \r moves cursor to start of line; trailing INDENT clears leftover chars
    print(f"\r> {text}" + INDENT)
    print(INDENT, end="", flush=True)


# Setup: create client, attach callbacks, connect
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883)

# Run MQTT loop in background thread (so we can receive while waiting for input)
thread = threading.Thread(target=client.loop_forever)
thread.daemon = True
thread.start()

# Main loop: read input and publish
try:
    while True:
        message = input()
        if message:
            full_message = f"[{MY_ID}] {message}"
            my_last_message = full_message
            client.publish(TOPIC, full_message)
        print(INDENT, end="", flush=True)
except KeyboardInterrupt:
    print("\nGoodbye!")
    client.disconnect()
