"""
This code is for the Raspberry Pi Pico board.

Scenario:

- The Raspberry Pi Pico board is connected to a computer via USB.
- The Raspberry Pi Pico board is running a MicroPython script.
- The MicroPython script is sending data to the computer via USB.
- The computer is running a Python Flask application that reads the data by specific script from the Raspberry Pi Pico board.
- The Python Flask application is storing the data in a database.
- The Python Flask application is displaying the data on a web page.
"""

import time, serial, datetime, json, random

SERIAL_PORT = "/dev/ttyACM0"
SERIAL_BAUDRATE = 9600

# Open the serial port
try:
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE)
    # Timeout for one second and flush the input buffer
    ser.timeout = 1
    ser.flushInput()
except serial.SerialException:
    print("Error: Could not open serial port.")
    exit()

while True:
    # Wait for the serial port to be ready
    while not ser.isOpen():
        time.sleep(1)
    
    # Create the data
    data = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temp": random.randint(-25, 45)
    }   

    # Send the data
    ser.write(json.dumps(data).encode())

    # Wait 20 seconds
    time.sleep(20)