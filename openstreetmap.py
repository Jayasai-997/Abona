from OSMPythonTools import Api
import pandas as pd
import pgeocode
from pyroutelib3 import Router
import matplotlib.pyplot as plt


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
    #try:
        plt.plot(int(startr[0]),int(startr[1]), 'ko')
        plt.plot(int(endr[0]), int(endr[1]), 'ro')
        #print(startr)
        startra.append(startr)
        endra.append(endr)


        router = Router("car")  # Initialise router
        start = router.findNode(int(startr[0]),int(startr[1]))  # Find start and end nodes
        end = router.findNode(endr[0],endr[1])
        print(start)
        print(end)
        status, route = router.doRoute(start, end)  # Find the route - a list of OSM nodes
        print(status)
        if status == 'success':
            routeLatLons = list(map(router.nodeLatLon, route))  # Get actual route coordinates
        print(routeLatLons)
        for i in routeLatLons:
            print(i[0],i[1])
            plt.plot(i[0],i[1], 'g.')
    #except:
     #   print('Fehler')


#########################
end = 5
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


