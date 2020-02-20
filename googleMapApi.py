import googlemaps as gm
from geopy.geocoders import GoogleV3


gmaps = gm.Client(key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")

def getCoordsWithAdress(address):
    res = gmaps.geocode(address)
    geo = res[0]['geometry']
    location = geo['location']
    lat = location['lat']
    lng = location['lng']
    return lat,lng




# Driver function
if __name__=="__main__":

    # Coorinates tuple.Can contain more than one pair.

    geolocator = GoogleV3(api_key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")
    fulladress = geolocator.reverse(getCoordsWithAdress("Los Barbechos 479, Las Condes, Chile"))
    if fulladress:
        print(fulladress[0].address)  # select first location


def main():
    pass


if __name__ == "__main__":
    main()

