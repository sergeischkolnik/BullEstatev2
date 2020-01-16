import googlemaps as gm
import reverse_geocoder

gmaps = gm.Client(key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")

def getCoordsWithAdress(address):
    res = gmaps.geocode(address)
    geo = res[0]['geometry']
    location = geo['location']
    lat = location['lat']
    lng = location['lng']
    return lat,lng

def getAdresswithCoords(lat,lon):
    res=reverse_geocoder.search((lat,lon))
    print(res)
def main():
    getAdresswithCoords(-33.408320, -70.573570)


if __name__ == "__main__":
    main()

