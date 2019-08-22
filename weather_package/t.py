#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import time
import socket
import sys
port = 9999

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

WEATHER_SYMBOL = {
    "Unknown":             u"✨",
    "Thunderstorm":        u"⛈",
    "Clouds":              u"☁️",
    "Fog":                 u"🌫",
    "Mist":                u"🌫",
    "Smoke":               u"🌫",
    "Haze":                u"🌫",
    "Dust":                u"🌫",
    "Sand":                u"🌫",
    "Ash":                 u"🌫",
    "Squall":              u"🌫",
    "Tornado":             u"🌪",
    "Rain":                u"🌧",
    "Snow":                u"❄️",
    "Drizzle":             u"🌧",
    "Clear":               u"☀️",
}

WIND_DIRECTION = [
    u"↓", u"↙", u"←", u"↖", u"↑", u"↗", u"→", u"↘",
]

def wind_directions():
    if data['wind']['deg'] == 0:
        return WIND_DIRECTION[0]
    if 0 < data['wind']['deg'] < 90:
        return WIND_DIRECTION[5]
    if data['wind']['deg'] == 90:
        return WIND_DIRECTION[4]
    if 90 < data['wind']['deg'] < 180:
        return WIND_DIRECTION[3]
    if data['wind']['deg'] == 180:
        return WIND_DIRECTION[2]
    if 180 < data['wind']['deg'] < 270:
        return WIND_DIRECTION[1]
    if data['wind']['deg'] == 270:
        return WIND_DIRECTION[0]
    if 270 < data['wind']['deg'] < 360:
        return WIND_DIRECTION[7]
    else: return WIND_DIRECTION[6]

def printClear():
    print "Weather Report: ", data['name'], ',' ,data['sys']['country']
    print "                " , Data
    print "\033[33m     \   /      \033[0m", data['weather'][0]['main'] , WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[33m     .---.      \033[0m", temp, '°C'
    print "\033[33m -― (     ) ―-  \033[0m", wind_direction, 'km/h'
    print '\033[33m     `---’      \033[0m' , humidity , '%'
    print '\033[33m     /   \      \033[0m', pressure , 'mBar'

def printClouds():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                " , Data
    print "\033[90m                \033[0m", data['weather'][0]['main'], WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[90m      .--.      \033[0m", temp, "°C"
    print "\033[90m   .-(    )_    \033[0m",wind_direction, "km/h"
    print '\033[90m  (___.__)__)   \033[0m', humidity, "%"
    print '\033[90m                \033[0m', data['main']['pressure'], "mBar"

def printFog():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                " , Data
    print "\033[90m                \033[0m", data['weather'][0]['main'], WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[90m   _ - _ - _ -  \033[0m", temp, "°C"
    print "\033[90m   _ - _ - _ -  \033[0m", wind_direction, "km/h"
    print '\033[90m   _ - _ - _ -  \033[0m', humidity, "%"
    print '\033[90m                \033[0m', data['main']['pressure'], "mBar"

def printRain():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                " , Data
    print "\033[90m       .--.     \033[0m", data['weather'][0]['main'], WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[90m    .-(    )_   \033[0m", temp, "°C"
    print "\033[90m   (___.___)__) \033[0m", wind_direction, "km/h"
    print '\033[34m    ‚‘‚‘‚‘‚‘    \033[0m', humidity, "%"
    print '\033[34m  ‚’‚’‚’‚’      \033[0m', pressure, "mBar"

def printStorm():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                " , Data
    print "\033[90m       .--.     \033[0m", data['weather'][0]['main'], WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[90m    .-(    )_   \033[0m", temp, "°C"
    print "\033[90m  (___.___)__)  \033[0m", wind_direction, "km/h"
    print '\033[33m    ‘⚡‘‘⚡‘‘     \033[0m', humidity, "%"
    print '\033[33m   ‘⚡‘⚡‘⚡‘      \033[0m', pressure, "mBar"

def printSnow():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                " , Data
    print "\033[90m       .--.     \033[0m", data['weather'][0]['main'], WEATHER_SYMBOL[data['weather'][0]['main']]
    print "\033[90m    .-(    )_   \033[0m", temp, "°C"
    print "\033[90m  (___.___)__)  \033[0m", wind_direction, "km/h"
    print '\033[0m    *   *   *    \033[0m', humidity, "%"
    print '\033[0m   *   *   *     \033[0m', pressure, "mBar"

def printClearNight():
    print "Weather Report: ", data['name'], ',', data['sys']['country']
    print "                ", Data
    print "\033[90m                \033[0m", data['weather'][0]['main'], '🌑'
    print "\033[90m      .--.      \033[0m", temp
    print "\033[90m     (    )     \033[0m", wind_direction, 'km/h'
    print '\033[90m      `--’      \033[0m', humidity, '%'
    print '\033[90m                \033[0m', pressure , 'mBar'

def showWeather():
    weatherTime = time.strftime("%H", time.localtime(int(data['dt'])))
    sunset = time.strftime("%H", time.localtime(int(data['sys']['sunset'])))
    if weatherTime >= sunset and data['weather'][0]['main'] == 'Clear' or data['weather'][0]['main'] == 'Unknown':
        printClearNight()
    if weatherTime < sunset and data['weather'][0]['main'] == 'Clear' or data['weather'][0]['main'] == 'Unknown':
        printClear()

    if data['weather'][0]['main'] == 'Clouds':
        printClouds()

    if data['weather'][0]['main'] == 'Fog' or data['weather'][0]['main'] == 'Mist' or data['weather'][0]['main'] == 'Smoke' or data['weather'][0]['main'] == 'Haze' or data['weather'][0]['main'] == 'Dust' or data['weather'][0]['main'] == 'Sand' or data['weather'][0]['main'] == 'Ash' or data['weather'][0]['main'] == 'Squall' or data['weather'][0]['main'] == 'Tornado':
        printFog()

    if data['weather'][0]['main'] == 'Snow':
        printSnow()

    if data['weather'][0]['main'] == 'Rain' or data['weather'][0]['main'] == 'Drizzle':
        printRain()

    if data['weather'][0]['main'] == 'Thunderstorm':
        printStorm()

def unixTimeConverter():
    return time.strftime("%a %d %b, %T", time.localtime(int(data['dt'])))


try:
    # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the client
    # client.connect((target, port))
    client.connect((get_ip(), port))
    # city name input
    city_name = ' '.join(str(name) for name in sys.argv[1:])
    if city_name == '':
	city_name = 'BeerSheba, IL'
    # send city name to server
    client.send(city_name)
    # receive data from weather api
    error = client.recv(1)
    if error == '1':
        print '\033[32mSorry, we are running out of queries to the weather service at the moment.'
        print 'Here is the weather report for the default city.\033[0m'
    if error == '2':
        print '\033[31mSorry, there is a problem connecting to the server. please try again later.\033[0m'
        exit(1)
    rec = client.recv(10000)
    data = json.loads(rec.decode("utf-8"))
    try:
    	# temperature
    	temp = data['main']['temp'] - 273.15
    except: 
	temp = 'unknown temperatue'
    try:
    	# wind direction
    	wind_direction = wind_directions() + ' ' + str(data['wind']['speed'] * 3.6)
    except KeyError:
        wind_direction = 'unknown direction'
    try:
    	Data = unixTimeConverter()
    except KeyError:
	Data = '00:00:00'
    try:
	humidity = data['main']['humidity']
    except KeyError:
	humidity = 'unknown humidity'
    try:
	pressure = data['main']['pressure']
    except KeyError:
	pressure = 'unknown pressure'
    showWeather()
    print
except ValueError:
    print '\033[31mAn error has occurred, please try again later.\033[0m'
except socket.error:
    print '\033[31mPlease check your internet connection...\033[0m'





'''
print '                                                       ┌─────────────┐                                                     '
print '┌──────────────────────────────┬───────────────────────┤             ├───────────────────────┬──────────────────────────────┐'
print '│                              │                       └──────┬──────┘                       │             Nuit             │'
print '├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤'
print '│                              │                              │                              │                              │'
print '│                              │                              │                              │                              │'
print '│                              │                              │                              │                              │'
print '│                              │                              │                              │                              |'
print '│                              │                              │                              │                              │'
print '└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘'



{
    "coord": 
     {
         "lon":-0.13,
         "lat":51.51
     }
    ,
    "weather":
        [{
            "id":300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
        }],
    "base": "stations",
    "main":
        {
            "temp": 280.32,
            "pressure":1012,
            "humidity":81,
            "temp_min":279.15,
            "temp_max":281.15
        },
    "visibility": 10000,
    "wind":
        {
            "speed":4.1,
            "deg":80
        },
    "clouds":
        {
            "all":90
        },
    "dt": 1485789600,
    "sys":
        {
            "type":1,
            "id":5091,
            "message":0.0103,
            "country":"GB",
            "sunrise":1485762037,
            "sunset":1485794875
        },
    "id":2643743,
    "name":"London",
    "cod":200
}
'''



