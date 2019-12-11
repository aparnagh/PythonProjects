'''
@date: 11/07/2019
@author: Aparna Ganesh

'''

import json
import urllib.request
import webbrowser, os
import time
from scapy.layers.inet import socket
from scapy.layers.inet import traceroute
from gmplot import gmplot   
import sys 

# list of latitudes
lats = []
# list of longitudes
longs = []
# list of colors for markers
colors = ['red', 'yellow', 'green', 'blue', 'black', 'white']
# list of IP addresses with no duplicates
noDuplicates = []

def create_coordinates_and_plot():
    # adds IP addresses with no duplicates
    for i in range (3, len(ips)):
        if i not in noDuplicates:
            noDuplicates.append(ips[i]);
    print(noDuplicates)
            
    for i in range (len(noDuplicates)):
        url = "http://dazzlepod.com/ip/{}.json".format(noDuplicates[i])
        print(url)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        if 'latitude' in data and 'longitude' in data:
            print(data)
            lats.append(data['latitude'])
            longs.append(data['longitude'])
    
                
    time.sleep(SLEEP_SECONDS)
    plot_lat_long()
        

def plot_lat_long():
   
    gmap = gmplot.GoogleMapPlotter(42.0167, 23.1000, 3)
    if ":\\" in gmap.coloricon:
        gmap.coloricon = gmap.coloricon.replace('/', '\\')
        gmap.coloricon = gmap.coloricon.replace('\\', '\\\\')
    
    for i in range(len(lats)):
        lat = lats[i]
        long = longs[i]
        colorIndex = i % (len(colors)-1)
        gmap.marker(lat, long, colors[colorIndex], None, i)
        
    gmap.plot(lats, longs, 'cornflowerblue', edge_width = 2.5)
    
    cwd = os.getcwd()
    
    gmap.draw("traceroute.html")

    webbrowser.open("file:///" + cwd +"/traceroute.html")
    
    
SLEEP_SECONDS = 2;

hostname = sys.argv[1]

ip = socket.gethostbyname(hostname)

res, _ = traceroute(ip,maxttl=64,verbose = 0)

ips = []

for item in res.get_trace()[ip]:
    ips.append(res.get_trace()[ip][item][0])
    
create_coordinates_and_plot()

