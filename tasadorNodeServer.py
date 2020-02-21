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

    }
print (tasacion)
try:
    print((geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"])))[0])
    tasacion["comuna"]= (geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"])).split(','))[1]
    tasacion["region"]= (geolocator.reverse(getCoordsWithAdress(tasacion["fulladdress"])).split(','))[2].replace('Region ','')
    comuna=tasacion["comuna"]
    lat,lon=getCoordsWithAdress(tasacion["fulladdress"])
    tasacion["lat"]=lat
    tasacion["lon"]=lon
    tasacion["tipotasacion"]="Full"
    tasaciontext=bpc.tasador(tasacion)

    print(tasaciontext)
    #print(tasacion)
    #print(tasacion["comuna"])
    #sys.stdout.flush()
except Exception as E:

    print(E)
   


 
[Location(Los Barbechos 479, Las Condes, Región Metropolitana, Chile, (-33.402217, -70.5608656, 0.0)),
Location(Los Barbechos 479, Las Condes, Región Metropolitana, Chile, (-33.402217, -70.5608656, 0.0)),
Location(Nuestra Señora del Rosario 397, Las Condes, Región Metropolitana, Chile, (-33.4021739, -70.5603974, 0.0)),
Location(Los Barbechos 431, Las Condes, Región Metropolitana, Chile, (-33.4024876, -70.5609707, 0.0)),
Location(Los Barbechos 401-437, Las Condes, Región Metropolitana, Chile, (-33.40251260000001, -70.5608103, 0.0)),
Location(Las Condes, Santiago Metropolitan Region, Chile, (-33.4079424, -70.5451063, 0.0)),
Location(Las Condes, Santiago Metropolitan Region, Chile, (-33.4087844, -70.567069, 0.0)),
Location(Santiago, Santiago Metropolitan Region, Chile, (-33.4488897, -70.6692655, 0.0)),
Location(Santiago Province, Santiago Metropolitan Region, Chile, (-33.45, -70.66669999999999, 0.0)),
Location(Santiago Metropolitan Region, Chile, (-33.4375545, -70.6504896, 0.0)),
Location(Chile, (-35.675147, -71.542969, 0.0))]
