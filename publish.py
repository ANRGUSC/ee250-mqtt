import paho.mqtt.publish as publish

publish.single("ee250", "Hello EE 250 folks", hostname="test.mosquitto.org")
print("Message published!")
