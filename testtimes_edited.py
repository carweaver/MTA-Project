#!/usr/bin/env python
import time
from bs4 import BeautifulSoup
import requests
import re
import json
twothreeURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/2/232?callback=angular.callbacks._0'
fourfiveURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/4/423?callback=angular.callbacks._0'


def Jsonify(trainURL):
    r = requests.get(trainURL)
    soup = BeautifulSoup(r.text,'html.parser')
    #json1 since need to call an actual json funtion later on
    json1 = soup.text
    json1 = json1.split('(')
    json1 = json1[1].split(')')
    json1 = json1[0]
    global jsonDict
    jsonDict = json.loads(json1)

def Info():
    updateTime = jsonDict["lastUpdatedTime"]
    station = jsonDict["stationName"]
    print(station, updateTime)
    print('----------')
    # print(updateTime)
    # print('----------')

def Uptown():
    uptowntext = ""
    manhattan = jsonDict["direction1"]["times"]
    if manhattan[0]["minutes"] > 0:
        uptowntext += str(manhattan[0]["route"])
        uptowntext += ":"
        uptowntext += str(manhattan[0]["minutes"])
        uptowntext += "min"
    elif manhattan[1]["minutes"] > 0:
        uptowntext += str(manhattan[1]["route"])
        uptowntext += ":"
        uptowntext += str(manhattan[1]["minutes"])
        uptowntext += "min"
    else:
        return "delayed"
    return uptowntext

def Downtown():
    downtowntext = ""
    brooklyn = jsonDict["direction2"]["times"]
    if brooklyn[0]["minutes"] > 0:
        downtowntext += str(brooklyn[0]["route"])
        downtowntext += ":"
        downtowntext += str(brooklyn[0]["minutes"])
        downtowntext += "min"
    elif brooklyn[1]["minutes"] > 0:
        downtowntext += str(brooklyn[1]["route"])
        downtowntext += ":"
        downtowntext += str(brooklyn[1]["minutes"])
        downtowntext += "min"
    else:
        return "delayed"   
    return downtowntext


def Uptown45():
    text = "Up"
    Jsonify(fourfiveURL)
    text += Uptown()
    return text
def Downtown45():
    text = "Down"
    Jsonify(fourfiveURL)
    text += Downtown()
    return text
def Uptown23():
    text = "Up"
    Jsonify(twothreeURL)
    text += Uptown()
    return text
def Downtown23():
    text = "Down"
    Jsonify(twothreeURL)
    text += Downtown()
    return text

subwaytimeslist = []
def runall():
    subwaytimeslist.append(Uptown23())
    subwaytimeslist.append(Uptown45())
    subwaytimeslist.append(Downtown23())
    subwaytimeslist.append(Downtown45())

runall()
print(subwaytimeslist)
