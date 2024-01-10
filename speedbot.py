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
    last_weather_file = 'last_weather.json'

    def load_last_weather():
        return json.load(open(last_weather_file))

    def save_last_weather(weather):
        json.dump(weather, open(last_weather_file, 'w'), indent=4)

    good__connection = False
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(base_url, timeout=5)
    except:
        data = load_last_weather()
    else:
        if response.status_code == 200:
            data = response.json()
            save_last_weather(data)
            good__connection = True
        else:
            data = load_last_weather()

    main = data['main']
    temperature = main['temp'] - 273.15
    humidity = main['humidity']

    return temperature, humidity, good__connection

while True:
    RESULT = 1000
    dl = 1000000000
    dt = datetime.now(tz=ZoneInfo('Europe/Berlin'))

    try:
        dl = st.download()
        temp, hum, gc = get_weather(api_key, city)
        RESULT = dl / 1000 / 1000
        gcs = '' if gc else '*'
        line = f'{dt}, {RESULT}, {round(temp, 2)}{gcs}, {round(hum)}\n'
        with open('speedbot.txt', 'a') as f:
            f.write(line)

        if RESULT == 1000 or RESULT < 100:
            sleep(60)
        else:
            sleep(60 * 5)

    except Exception as e:
        line = f'{dt}, {e} ({dl})\n'
        with open('speedbot_e.txt', 'a') as f:
            f.write(line)
        sleep(60)
