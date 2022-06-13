import requests
import folium
import polyline
import pandas as pd



def get_route(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat):
    url = "http://127.0.0.1:5000/route/v1/driving/{},{};{},{}?steps=true".format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
    r = requests.get(url)
    if r.status_code != 200:
        return {}

    res = r.json()
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']

    out = {'route': routes,
           'start_point': start_point,
           'end_point': end_point,
           'distance': distance
           }

    return out


def get_map(route):
    m = folium.Map(location=[(route['start_point'][0] + route['end_point'][0]) / 2,
                             (route['start_point'][1] + route['end_point'][1]) / 2],
                   zoom_start=13)

    folium.PolyLine(
        route['route'],
        weight=8,
        color='blue',
        opacity=0.6
    ).add_to(m)

    folium.Marker(
        location=route['start_point'],
        icon=folium.Icon(icon='play', color='green')
    ).add_to(m)

    folium.Marker(
        location=route['end_point'],
        icon=folium.Icon(icon='stop', color='red')
    ).add_to(m)



    return m

df = pd.read_csv('check.csv')

#df['location'] = df.apply(lambda x: get_route(x['s_lon'],x['s_lat'],x['d_lon'],x['d_lat']),axis=1)
#df['routes'] = df['location'].apply(lambda x: x['route'])
#df['dist'] = df['location'].apply(lambda x: x['distance'])
#df.to_csv('routes.csv',index=False)



