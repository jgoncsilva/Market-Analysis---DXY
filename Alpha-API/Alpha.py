
import requests
import re
import csv
import pandas as pd
import urllib.request, json
import time
import matplotlib.pyplot as plt

key = 'NWGOGUGXN2IFYE6ONWGOGUGXN2IFYE6O'

inputs = { 
    'function': 'TIME_SERIES_WEEKLY_ADJUSTED',
    'symbol' : 'DXY',
    'datatype': 'json',
    'apykey' : key
}

url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=DXY&apikey=NWGOGUGXN2IFYE6ONWGOGUGXN2IFYE6ONWGOGUGXN2IFYE6ONWGOGUGXN2IFYE6O"

response = urllib.request.urlopen(url)
#from  var saved(HTTPresponse Type), use . read() + decode('utf-8')
string = response.read().decode('utf-8')
#Load string saved into json
jsondata = json.loads(string)

print(jsondata)

jsondata['Meta Data

def _output_formats(cls, func, override =None):]