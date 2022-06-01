#pip install pyroutelib3
#https://github.com/MKuranowski/pyroutelib3
#API to route in OpenStreetmap using GPS coordinates

from pyroutelib3 import Router # Import the router
router = Router("car") # Initialise it

start = router.findNode(47.66282, 9.48308) # Find start and end nodes
end = router.findNode(47.66501, 9.47003)
#print(start)
status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes
#print(status)
if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
print(routeLatLons)
