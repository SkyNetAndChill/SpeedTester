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
