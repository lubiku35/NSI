"""
This code is for the Raspberry Pi Pico board.

Scenario:

1. Connect to a Wi-Fi network.
2. Connect to an MQTT broker.
3. Publish random temperature data every minute.

"""

import network, time, random, utime, json
from simple import MQTTClient

WIFI=""
PASS=""
CLIENT_ID="RPI-Pico-W"
SERVER=b""
PORT=""

def get_formatted_time():
    year, month, mday, hour, minute, second, weekday, yearday = utime.localtime()[:8]
    return f"{year}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(WIFI, PASS)

while wlan.isconnected() == False:
    print('Waiting for connection')
    time.sleep(2)

print(f"Connection Successful: {wlan.ifconfig()}")

try:
    client = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=int(PORT))
    client.connect()
except Exception as e:
    print("Error connecting to MQTT:", e)
    raise


while True:
    data = {
        "temp": round(random.uniform(-10, 40), 2),
        "timestamp": get_formatted_time()
    }
    
    json_data = json.dumps(data)
    
    client.publish("/test", json_data)

    time.sleep(60)

