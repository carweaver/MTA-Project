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
    print()
    print(station, updateTime)
    print('----------')
    # print(updateTime)
    # print('----------')

def Uptown():
    manhattan = jsonDict["direction1"]["times"][0:2]
    for i in range(0,2):
        NextTrainsManhattan = ("There is a", manhattan[i]["route"], "train to", manhattan[i]["lastStation"],":", manhattan[i]["minutes"], "minutes away")
        print(*NextTrainsManhattan)
    print()

def Downtown():
    brooklyn = jsonDict["direction2"]["times"][0:2]
    for j in range(0,2):
        NextTrainsBrooklyn = ("There is a", brooklyn[j]["route"], "train to", brooklyn[j]["lastStation"],":", brooklyn[j]["minutes"], "minutes away")
        print(*NextTrainsBrooklyn)
    print()

def main(): 
    Jsonify(twothreeURL)
    Info()
    print(jsonDict["direction1"]["name"])
    Uptown()
    Jsonify(fourfiveURL)
    Uptown()
    print('---------')
    Jsonify(twothreeURL)
    print(jsonDict["direction2"]["name"])
    Downtown()
    Jsonify(fourfiveURL)
    Downtown()
main() # set time limit
