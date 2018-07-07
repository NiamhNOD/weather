import requests
import json
import datetime
import time
import sqlite3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

darkskyKey = config['darksky']['darkskyKey']

currentTime = datetime.datetime.now()
seconds = time.time()
seconds = int(seconds)
secondsStr = str(seconds)
weather_cork_response = requests.get('https://api.darksky.net/forecast/' + darkskyKey + '/51.8498,-8.3959,' + secondsStr + '?exclude=currently,minutely,daily,alerts,flags&units=uk2')

weather_cork_json = weather_cork_response.json()

time = seconds

for i in weather_cork_json:
    print('in json')
    if i == 'hourly':
        print('in hourly')
        for j in weather_cork_json[i]:
            if j == 'summary':
                summary = weather_cork_json[i][j]
            if j == 'icon':
                icon = weather_cork_json[i][j]
            if j == 'data':
                for l in weather_cork_json[i][j][0]:
                    if l == 'precipIntensity':
                        precipIn = weather_cork_json[i][j][0][l]
                    elif l == 'precipProbability':
                        precipProb = weather_cork_json[i][j][0][l]
                    elif l == 'temperature':
                        temp = weather_cork_json[i][j][0][l]
                    elif l == 'apparentTemperature':
                        appTemp = weather_cork_json[i][j][0][l]
                    elif l == 'humidity':
                        hum = weather_cork_json[i][j][0][l]
                    elif l == 'pressure':
                        press = weather_cork_json[i][j][0][l]
                    elif l == 'windSpeed':
                        windS = weather_cork_json[i][j][0][l]
                    elif l == 'windBearing':
                        windB = weather_cork_json[i][j][0][l]
                    elif l == 'cloudCover':
                        cloudC = weather_cork_json[i][j][0][l]

conn = sqlite3.connect('weathercork.db')
c = conn.cursor()
c.execute("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (time, summary, icon, precipIn, precipProb, temp, appTemp, hum, press, windS, windB, cloudC))
conn.commit()
conn.close()
print(datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%D - %H:%M'))
