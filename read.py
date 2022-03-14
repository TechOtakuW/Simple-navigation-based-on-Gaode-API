from typing import Collection
import xml.dom.minidom as xdom

gpxPath = 'test.gpx'
dom_tree = xdom.parse(gpxPath)
Collection = dom_tree.documentElement
trkpts = Collection.getElementsByTagName("trlpt")
lats, lons = [], []

for trkpt in trkpts:
    lat = trkpt.getAttribute("lat")
    lon = trkpt.getAttribute("lon")
    if lat=='0' or lon=='0':
        continue
    lats.append(float(lat))
    lons.append(float(lon))

datas = {'lat': lats, 'lon':lons}

