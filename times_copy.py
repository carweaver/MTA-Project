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
    manhattan = jsonDict["direction1"]["times"][0:2]
    for i in range(0,2):
        # NextTrainsManhattan = ("There is a", manhattan[i]["route"], "train to", manhattan[i]["lastStation"],":", manhattan[i]["minutes"], "minutes away")
        uptowntext += str(manhattan[i]["route"])
        uptowntext += " train in "
        uptowntext += str(manhattan[i]["minutes"])
        uptowntext += " min  "
        return uptowntext

def Downtown():
    downtowntext = ""
    brooklyn = jsonDict["direction2"]["times"][0:2]
    for j in range(0,2):
        # NextTrainsBrooklyn = ("There is a", brooklyn[j]["route"], "train to", brooklyn[j]["lastStation"],":", brooklyn[j]["minutes"], "minutes away")
        downtowntext += str(brooklyn[j]["route"])
        downtowntext += " train in "
        downtowntext += str(brooklyn[j]["minutes"])
        downtowntext += " min  "
        return downtowntext

def AllUptown():
    totaluptowntext = ""
    Jsonify(twothreeURL)
    Info()
    totaluptowntext += Uptown()
    Jsonify(fourfiveURL)
    totaluptowntext += Uptown()
    print(totaluptowntext)
    return totaluptowntext

def AllDowntown():
    totaldowntowntext = "" 
    Jsonify(twothreeURL)
    totaldowntowntext += Downtown()
    Jsonify(fourfiveURL)
    totaldowntowntext += Downtown()
    print(totaldowntowntext)
    return totaldowntowntext


