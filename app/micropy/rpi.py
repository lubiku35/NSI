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

import time, json, random, utime

def get_formatted_time():
    year, month, mday, hour, minute, second, weekday, yearday = utime.localtime()[:8]
    return f"{year}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}"

while True:
    data = {
        "temp": round(random.uniform(-10, 40), 2),
        "timestamp": get_formatted_time()
    }
    
    json_data = json.dumps(data)
    
    print(b'' + json_data.encode())

    time.sleep(60)
