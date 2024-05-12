"""
Purpose: This module is responsible for listening to the Raspberry Pi Pico board and storing the data in a database.
"""

import time, serial, json, requests

# Serial port configuration
SERIAL_PORT = "/dev/ttyACM0"
SERIAL_BAUDRATE = 115200
APP_URL = "http://localhost:5000"
API_URL = f"{APP_URL}/api/item"

def send_data(data):
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Data stored: {data}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

try:
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    ser.flushInput()
except serial.SerialException:
    print("Error: Could not open serial port.")
    exit()

import time, serial, json

while True:
    if ser.isOpen():
        try:
            raw_data = ser.readline()
            print(f"Raw data: {raw_data}")
            decoded_data = raw_data.decode('utf-8').strip()
            if decoded_data:
                print(f"Received data: {decoded_data}")  # Ensure this is the decoded string
                data = json.loads(decoded_data)
                print(f"Data loaded: {data}")  # Confirm data is loaded correctly
                send_data(data)
            else:
                print("Received empty string.")
        except UnicodeDecodeError as e:
            print(f"Error: Could not decode data. Raw data received: {raw_data}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format. Decoded data received: '{decoded_data}'")
        except Exception as e:
            print(f"Unexpected error: {e}")
    time.sleep(1)