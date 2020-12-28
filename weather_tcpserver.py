#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
from socket import *
import thread
import time

BUFF = 1024
HOST = '127.0.0.1'
PORT = 9999 

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def handler(clientsock, addr):
    try:
        city_name = clientsock.recv(BUFF)
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=bce0e560d0b631a58040daa6546eed48'
        json_obj1 = urllib2.urlopen(url)
        data = json.load(json_obj1)
        json_data = json.dumps(data).encode("utf-8")
        clientsock.send('0')
        clientsock.send(json_data)
    except:
        try:
            clientsock.send('1')
            city_name = 'BeerSheba, IL'
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=bce0e560d0b631a58040daa6546eed48'
            json_obj1 = urllib2.urlopen(url)
            data = json.load(json_obj1)
            json_data = json.dumps(data).encode("utf-8")
            clientsock.send(json_data)
        except:
            clientsock.send('2')
    clientsock.close()



ADDR = (get_ip(), PORT)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serversock.bind(ADDR)
serversock.listen(5)
while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    print addr , " connected"
    thread.start_new_thread(handler, (clientsock, addr))
