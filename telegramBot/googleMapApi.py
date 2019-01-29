import googlemaps as gm
gmaps = gm.Client(key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")

def getCoordsWithAdress(address):
    res = gmaps.geocode(address)
    geo = res[0]['geometry']
    location = geo['location']
    lat = location['lat']
    lng = location['lng']
    return lat,lng