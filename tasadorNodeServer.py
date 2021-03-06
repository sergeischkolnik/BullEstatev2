import sys
import googlemaps as gm
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(api_key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")

import botPropertyConnector as bpc
gmaps = gm.Client(key="AIzaSyDnRrlFVxG-1-WspdF-qX3PVJo0q_JqgtY")

def getCoordsWithAdress(address):
    res = gmaps.geocode(address)
    geo = res[0]['geometry']
    location = geo['location']
    lat = location['lat']
    lng = location['lng']
    return lat,lng
tasacion={}
text=''

for i in sys.argv:
    print (i)

tasacion={
    "tipo":sys.argv[1],
    "fulladdress":sys.argv[2],
    "apt":sys.argv[3],
    "dormitorios":sys.argv[4],
    "baños":sys.argv[5],
    "estacionamientos":sys.argv[6],
    "bodegas":sys.argv[7],
    "metros":sys.argv[8],
    "total":sys.argv[9],
    "firstname":sys.argv[10],
    "lastname":sys.argv[11],
    "rut":sys.argv[12],
    "mail":sys.argv[13],
    "phone":sys.argv[14],
    "profile":sys.argv[15],
    "interest":sys.argv[16],
    "adress":sys.argv[2],
    "tipotasacion":sys.argv[17],

    }
print (tasacion)
try:
    print((geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"])))[0])
    tasacion["comuna"]= ((str(geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"]))[0]).split(','))[1])[1:]
    print(tasacion["comuna"])
    tasacion["region"]= (str(geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"]))[0]).split(','))[2].replace(' Región ','')
    print(tasacion["region"])
    comuna=tasacion["comuna"]
    lat,lon=getCoordsWithAdress(tasacion["fulladdress"])
    tasacion["lat"]=lat
    tasacion["lon"]=lon

    print("entering bpc")
    tasaciontext=bpc.tasador(tasacion)
    print("succeed")
    print(tasaciontext)
    #print(tasacion)
    #print(tasacion["comuna"])
    #sys.stdout.flush()
except Exception as E:
    print("fail")
    print(E)
   



