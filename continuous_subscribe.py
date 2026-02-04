import paho.mqtt.client as mqtt

TOPIC = "ee250"
BROKER = "test.mosquitto.org"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to {BROKER}")
        client.subscribe(TOPIC)
        print(f"Subscribed to '{TOPIC}'. Waiting for messages... (Ctrl+C to exit)")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"({msg.topic}, {msg.payload})")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnecting...")
    client.disconnect()
