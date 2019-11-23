# Area de importacion
import requests
import pandas
import plotly.express as px
import fastkml
import  pykml
import urllib3
from lxml import html
import folium

from zipfile import  ZipFile
from lxml import html
kmz = ZipFile('./049-E5-49.kmz','r')
kml = kmz.open('doc.kml','r').read()

doc = html.fromstring(kml)
for pm in doc.cssselect('Folder Document Placemark'):
    temp = pm.cssselect('track')
    name = pm.cssselect('name')[0].text_content()
    if len(temp):
        temp=temp[0]
        for desc in temp.iterdescendants():
            content = desc.text_content()
            if desc.tag == 'when':
                do_timestamp_stuff(content)
            elif desc.tag == 'coord':
                do_coordinate_stuff(content)
            else:
                print("Skipping empty tag %s" % desc.tag)
    else:
        # Reference point Placemark
        coord = pm.cssselect('Point coordinates')[0].text_content()
        do_reference_stuff(coord)

north = df_buses[df_buses['Direction']=='NORTH']
south = df_buses[df_buses['Direction']=='SOUTH']
east = df_buses[df_buses['Direction']=='EAST']
west = df_buses[df_buses['Direction']=='WEST']

north_gps = north[['Latitude','Longitude']]
north_poslist= north_gps.values.tolist()
north_poslist

map2 = folium.Map(location=[49.27565, -122.798683], tiles='CartoDB dark_matter', zoom_start=10)
marker_cluster = folium.CircleMarker()#.add_to(map2)

for point in range(0,len(north_poslist)):
    folium.Marker(north_poslist[point], popup=north[['RouteNo','Destination','Pattern','Latitude','Longitude','Direction']]).add_to(map2)
map2