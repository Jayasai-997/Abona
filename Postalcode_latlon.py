import pgeocode
from pyroutelib3 import Router
import pandas as pd
from tqdm import tqdm
tqdm.pandas(desc="Progress!")

df = pd.read_csv('Refromate_data.csv', on_bad_lines='skip',encoding='latin-1', sep=',')
print(df.shape)
df.dropna(inplace=True)
def GPS_aus_PLZ(Land, PLZ):
    try:
        nomi = pgeocode.Nominatim(Land)
        return nomi.query_postal_code(PLZ).latitude, nomi.query_postal_code(PLZ).longitude
    except:
        pass

def route(source,destination):
  router = Router("car") # Initialise it

  start = router.findNode(source[0],source[1]) # Find start and end nodes
  end = router.findNode(destination[0],destination[1])

  status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes
  if status == 'success':
      routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates

  return routeLatLons
#
# df["Source"] = df.progress_apply(lambda x: GPS_aus_PLZ(x["Abfahrtsland"],x["Abfahrtspostleitzahl"]),axis=1)
# df["Destination"] = df.progress_apply(lambda x: GPS_aus_PLZ(x["Ankunftsland"],x["Ankunftspostleitzahl"]),axis=1)
#
#df.to_csv('Refromate_data.csv')

df.isnull().sum()

df[df.isna().any(axis=1)]
#df.to_csv('Cleaned_data.csv')
#DataTypes = df.dtypes
#print(df.iloc[8:])
start_coordinates = df.iloc[:, 9].tolist()
desti_coordinates = df.iloc[:, 10].tolist()

#df["Route"] = df.progress_apply(lambda x: route(x["Sources"], x["Destination"]),axis=1)

#geo_coordinates = route((48.5039, -4.2400416666666665), (44.3987, 2.024753846153846))

#print(geo_coordinates)
#print(df["Route"])
