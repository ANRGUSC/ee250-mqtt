# EE250 MQTT Chat Demo

A simple MQTT publish/subscribe chat application demonstrating the pub/sub messaging pattern using the Eclipse Paho MQTT library.

## Overview

This project contains several Python scripts that demonstrate MQTT messaging:

- **chat.py** - Interactive chat application where multiple users can send/receive messages
- **publish.py** - Simple one-shot message publisher
- **subscribe.py** - Simple one-shot message subscriber (receives one message and exits)
- **continuous_subscribe.py** - Continuous subscriber that listens for messages indefinitely

All scripts connect to the public `test.mosquitto.org` broker on port 1883 using the topic `ee250`.

## Requirements

- Python 3.x
- paho-mqtt library

## Installation

### Ubuntu/Debian

```bash
# Install the MQTT library via apt
sudo apt update
sudo apt install python3-paho-mqtt

# Clone the repo
git clone https://github.com/ANRGUSC/ee250-mqtt.git
cd ee250-mqtt
```

### Using pip (any platform)

```bash
# Clone the repo
git clone https://github.com/ANRGUSC/ee250-mqtt.git
cd ee250-mqtt

# Option A: Install globally
pip install paho-mqtt

# Option B: Use a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
# or: venv\Scripts\activate   # Windows
pip install paho-mqtt
```

## Usage

### Interactive Chat

```bash
python3 chat.py
```

Messages you send appear indented on the right. Messages from others appear on the left with their session ID.

### Basic Publish/Subscribe

In one terminal:
```bash
python3 subscribe.py
```

In another terminal:
```bash
python3 publish.py
```

### Continuous Monitoring

```bash
python3 continuous_subscribe.py
```

Press `Ctrl+C` to exit.

## How It Works

MQTT is a lightweight publish/subscribe messaging protocol. In this demo:

1. Clients connect to a broker (`test.mosquitto.org`)
2. Subscribers listen on a topic (`ee250`)
3. Publishers send messages to that topic
4. The broker routes messages to all subscribers

## License

This project is licensed under the Polyform Noncommercial License 1.0.0 - see [LICENSE.md](LICENSE.md) for details.
