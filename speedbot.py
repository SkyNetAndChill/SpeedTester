"""
This module contains a script for monitoring internet speed and weather conditions.

It uses the speedtest and OpenWeatherMap APIs to gather data about the current download speed and weather conditions, respectively.
The data is then written to a file for later analysis.

Functions:
    get_weather(api_key, city): Returns the current temperature and humidity for the specified city.

Global Variables:
    st: A Speedtest client instance.
    config: A dictionary containing configuration data loaded from 'config.json'.
    api_key: The API key for OpenWeatherMap, loaded from 'config.json'.
    city: The city for which to get weather data, loaded from 'config.json'.

The script runs indefinitely, checking the download speed and weather conditions every 5 minutes, or every minute if the download speed is less than 100 Mbps or if an error occurs.

SkyNetAndChill 2023
"""

from time import sleep
from datetime import datetime
from zoneinfo import ZoneInfo
import speedtest
import requests
import json

st = speedtest.Speedtest()

config = json.load(open('config.json'))
api_key = config['api_key']
city = config['city']


def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url, timeout=5)

    if response.status_code == 200:

        data = response.json()

        main = data['main']
        temperature = main['temp'] - 273.15
        humidity = main['humidity']

        return temperature, humidity
    else:
        return "", ""

while True:
    RESULT = 1000
    dl = 1000000000
    dt = datetime.now(tz=ZoneInfo('Europe/Berlin'))

    try:
        dl = st.download()
        temp, hum = get_weather(api_key, city)
        RESULT = dl / 1000 / 1000
        line = f'{dt}, {RESULT}, {round(temp, 2)}, {round(hum)}\n'
    except Exception as e:
        line = f'{dt}, {e} ({dl})\n'
        with open('speedbot_e.txt', 'a') as f:
            f.write(line)

    with open('speedbot.txt', 'a') as f:
        f.write(line)
    with open('speedbot_e.txt', 'a') as f:
        f.write(line)

    if RESULT == 1000 or RESULT < 100:
        sleep(60)
    else:
        sleep(60 * 5)
