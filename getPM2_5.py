#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
A simple program for demonstration of json.
"""

import urllib
import json

# url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=100&format=json"
url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&format=json"
urllib.urlretrieve(url, "data.txt")
f = open('data.txt', 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)
print data
inx = 0
for j in data:
    print str(inx) + ' ' + j["SiteName"] + " " + j["County"] + " PM2.5: " + j["PM2.5"]
    inx += 1
