import requests
import json
import time
import sqlite3
import configparser

def getForecastCork(darkskyKey):
    # Get the time for the API request from Darkysky
    seconds = time.time()
    # Request the JSON from Darksky
    weather_cork_response = requests.get('https://api.darksky.net/forecast/'
    + darkskyKey + '/51.8498,-8.3959,' + str(int(seconds))
    + '?exclude=currently,hourly,minutely,alerts,flags&units=uk2')
    weather_cork_json = weather_cork_response.json()

    # Loop over the Darksky JSON getting the individual data
    for j in weather_cork_json['daily']['data'][0]:
        if j == 'time':
            localTime = weather_cork_json['daily']['data'][0][j]
        elif j == 'summary':
            summary = weather_cork_json['daily']['data'][0][j]
        elif j == 'icon':
            icon = weather_cork_json['daily']['data'][0][j]
        elif j == 'sunriseTime':
            sunriseTime = weather_cork_json['daily']['data'][0][j]
        elif j == 'sunsetTime':
            sunsetTime = weather_cork_json['daily']['data'][0][j]
        elif j == 'precipIntensity':
            precipIn = weather_cork_json['daily']['data'][0][j]
        elif j == 'precipProbability':
            precipProb = weather_cork_json['daily']['data'][0][j]
        elif j == 'temperatureHigh':
            tempHigh = weather_cork_json['daily']['data'][0][j]
        elif j == 'temperatureLow':
            tempLow = weather_cork_json['daily']['data'][0][j]
        elif j == 'humidity':
            hum = weather_cork_json['daily']['data'][0][j]
        elif j == 'pressure':
            press = weather_cork_json['daily']['data'][0][j]
        elif j == 'windSpeed':
            windS = weather_cork_json['daily']['data'][0][j]
        elif j == 'windBearing':
            windB = weather_cork_json['daily']['data'][0][j]
        elif j == 'cloudCover':
            cloudC = weather_cork_json['daily']['data'][0][j]

    # Connect to the Database
    conn = sqlite3.connect('weathercork.db')
    c = conn.cursor()

    # Execute and commit that database query
    c.execute("INSERT INTO weatherDaily VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
    (localTime, summary, icon, sunriseTime, sunsetTime, precipIn,
     precipProb, tempHigh, tempLow, hum, press, windS, windB, cloudC))
    conn.commit()
    conn.close()
