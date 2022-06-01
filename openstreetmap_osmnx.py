from OSMPythonTools.api import Api
import pandas as pd
import pgeocode
from pyroutelib3 import Router
import geopandas as gpd
import networkx as nx
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import sklearn.neighbors

#https://geoffboeing.com/2016/11/osmnx-python-street-networks/
#https://osmnx.readthedocs.io/en/stable/index.html

Sheet = 'Datensatz_01_2021.csv'
Data = []
f = open (Sheet, 'r', encoding='iso8859')
Datensatz = f.readlines()
for row in Datensatz:

    #row = row.replace(';"', '')
    #row = row.replace('"', '')
    rowdict =row.strip().split(';')
    if len(rowdict) == 8:
        for i in range(10):
            rowdict[1]=rowdict[1].replace(str(i), '')
            rowdict[5] = rowdict[5].replace(str(i), '')
        Data.append(rowdict)
    if len(rowdict) != 8:
        #print(rowdict)
        pass
f.close()
#print(Data)
###########################
#Convert Land + postal Code to GPS
def GPS_aus_PLZ(Land, PLZ):
    try:
        nomi = pgeocode.Nominatim(Land)
        #print(Land, PLZ)
        #print(nomi.query_postal_code(PLZ).longitude, nomi.query_postal_code(PLZ).latitude)
        return nomi.query_postal_code(PLZ).latitude, nomi.query_postal_code(PLZ).longitude
    except:
        pass

#########################
startra = []
endra = []
def Route(startr, endr):

    plt.plot(int(startr[0]),int(startr[1]), 'ko')
    plt.plot(int(endr[0]), int(endr[1]), 'ro')



    origin_point = startr
    destination_point = endr
    #mode = "drive"
    #G = ox.graph_from_point(origin_point, dist=2000, simplify=True, network_type=mode)
    G = ox.graph_from_bbox(40, 50, -5, 10, network_type='drive')


    G = ox.graph_from_bbox(37.79, 37.78, -122.41, -122.43, network_type='drive')
    G_projected = ox.project_graph(G)
    ox.plot_graph(G_projected)

    origin_node = ox.get_nearest_node(G, origin_point)
    destination_node = ox.get_nearest_node(G, destination_point)

    route = ox.shortest_path(G, origin_node, destination_node)
    #bbox = ox.utils_geo.bbox_from_point(point=destination_point, dist=700)
    #fig, ax = ox.plot_graph_route(G, route, bbox=bbox, route_linewidth=6, node_size=0, bgcolor='k')
    ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, bgcolor='w')

#########################
end = 3
df = pd.DataFrame(Data)
df.columns = df.iloc[0]
df = df[1:end]
print(df)
###########################

List = [[GPS_aus_PLZ(a,b), GPS_aus_PLZ(c,d)] for a,b,c,d in zip(df['Ankunftsland'],df['Ankunftspostleitzahl'],df['Abfahrtsland'],df['Abfahrtspostleitzahl'])]
R =[Route(*l) for l in List]
print(List)
#print(startra)
#print(endra)
#print(len(startra), len(endra))
plt.show()
if __name__ == '__main__':
    pass
    #print(Datensatz)


