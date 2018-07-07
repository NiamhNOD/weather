import requests
import json
import time
import sqlite3
import configparser

def loadDarkskyKey():
    # Open the config file to read in the Darksky key
    config = configparser.ConfigParser()
    config.read('config.ini')
    darkskyKey = config['darksky']['darkskyKey']
    return darkskyKey


def getCurrentWeatherCork(darkskyKey):
    # Get the time for the API request from Darkysky
    seconds = time.time()
    # Request the JSON from Darksky
    weather_cork_response = requests.get('https://api.darksky.net/forecast/' + darkskyKey + '/51.8498,-8.3959,' + str(int(seconds)) + '?exclude=hourly,minutely,daily,alerts,flags&units=uk2')
    weather_cork_json = weather_cork_response.json()

    # Loop over the Darksky JSON getting the individual data
    for i in weather_cork_json:
        if i == 'currently':
            for j in weather_cork_json[i]:
                if j == 'summary':
                    summary = weather_cork_json[i][j]
                elif j == 'icon':
                    icon = weather_cork_json[i][j]
                elif j == 'precipIntensity':
                    precipIn = weather_cork_json[i][j]
                elif j == 'precipProbability':
                    precipProb = weather_cork_json[i][j]
                elif j == 'temperature':
                    temp = weather_cork_json[i][j]
                elif j == 'apparentTemperature':
                    appTemp = weather_cork_json[i][j]
                elif j == 'humidity':
                    hum = weather_cork_json[i][j]
                elif j == 'pressure':
                    press = weather_cork_json[i][j]
                elif j == 'windSpeed':
                    windS = weather_cork_json[i][j]
                elif j == 'windBearing':
                    windB = weather_cork_json[i][j]
                elif j == 'cloudCover':
                    cloudC = weather_cork_json[i][j]

    # Connect to the Database
    conn = sqlite3.connect('weathercork.db')
    c = conn.cursor()

    # Execute and commit that database query
    c.execute("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (int(seconds), summary, icon, precipIn, precipProb, temp, appTemp, hum, press, windS, windB, cloudC))
    conn.commit()
    conn.close()

    print('The current temperature is ' + str(temp) + 'C. It feels like ' + str(appTemp) + "C.")
