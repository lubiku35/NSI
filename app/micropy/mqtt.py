# mqtt_subscriber.py
import paho.mqtt.client as mqtt
import threading, requests, json

# MQTT settings
MQTT_BROKER = "localhost"
MQTT_PORT = 3510  
MQTT_TOPIC = "/data"

# API settings
API_URL = "http://localhost:5000/api/item"

# Global variable to store the latest message
latest_message = None

# API settings
def send_data(data):
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Data stored: {data}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def validate_data(data):
    if "temp" in data and "timestamp" in data:
        # check if temp is a float and timestamp is a string
        if isinstance(data["temp"], float) and isinstance(data["timestamp"], str):
            return True
    return False

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global latest_message
    latest_message = msg.payload.decode('utf-8')
    print(f"Received message on {msg.topic}: {latest_message}")
    try:
        data = json.loads(latest_message)
        if validate_data(data):
            send_data(data)
        else:
            print("Invalid data format.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")    

# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Run MQTT client in a separate thread
def run_mqtt():
    mqtt_client.loop_forever()

mqtt_thread = threading.Thread(target=run_mqtt)
mqtt_thread.start()

# Function to get the latest message
def get_latest_message():
    global latest_message
    return latest_message