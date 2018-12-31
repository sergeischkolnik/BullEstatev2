import numpy as np
from pandas import DataFrame
from sklearn import linear_model
import csvReader as cvsR
import csvWriter as cvsW
import datetime

def distance(x1,y1,x2,y2):
    return ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5

print(str(datetime.datetime.now().time()))

promediosDeltas = []
ks = []


propsArriendos =  cvsR.readCsvSinFiltrosBasicosArriendos('arriendos.csv')

propsVentas = cvsR.readCsvSinFiltrosBasicosVentas('ventas.csv')

largoVentas = len(propsVentas)


#propsDist = np.zeros(shape=(len(propsVentas), len(propsArriendos)))

# print("Filling distance matrix")
# largo = len(propsVentas)
# for i,p in enumerate(propsVentas):
#     print(str(i) + '/' + str(largo))
#     for j,p2 in enumerate(propsArriendos):
#         propsDist[i,j] = distance(float(p[7]),float(p[8]),float(p2[7]),float(p2[8]))



print("Loading dist matrix")
propsDist = np.load("distMatrix.npy")


k = 20

neighbors = []
for i,p in enumerate(propsVentas):
    print("creating neighbor list "+ str(i) + "/" + str(largoVentas))
    row = propsDist[i, :]
    sortedIdsByLowestDistance = np.argsort(row)
    nrNeighs = 0
    neighList = []
    for it in range(0,len(sortedIdsByLowestDistance)):
        candidato = propsArriendos[sortedIdsByLowestDistance[it]]
        if p[3] == candidato[3] and  p[4] == candidato[4]:
            neighList.append(sortedIdsByLowestDistance[it])
            nrNeighs += 1
            if nrNeighs == k:
                break

    neighbors.append(neighList)

predictions = []

for i, prop in enumerate(propsVentas):
    print("calculating predictions for each property" + str(i) + "/" + str(largoVentas))
    bedrooms = []
    prices = []
    baths = []
    sqtfts = []
    for neighbor in neighbors[i]:
        #para cada vecino, lo tomo para meterlo a la regresion
        nIndex = int(neighbor)
        nObj = propsArriendos[nIndex]
        nrBedRms = int(nObj[3])
        bedrooms.append(nrBedRms)
        price = nObj[2]
        prices.append(price)
        bath = int(nObj[4])
        baths.append(bath)
        sqtft = nObj[6]
        sqtfts.append(sqtft)

    Properties = {
        'bedrooms': bedrooms,
        'price': prices,
        'baths': baths,
        'sqft' : sqtfts
        }

    df = DataFrame(Properties, columns=['bedrooms', 'baths', 'sqft', 'price'])

    X = df[['bedrooms','baths','sqft']].astype(float) # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
    Y = df['price'].astype(float)

    # with sklearn
    regr = linear_model.LinearRegression()
    if len(X) == 0 or len(Y)==0:
        prop.append(0)
        continue
    regr.fit(X, Y)

    # prediction with sklearn
    New_bedrooms = int(prop[3])
    New_baths = int(prop[4])
    New_sqft =  float(prop[5])
    prop.append(float(regr.predict([[New_bedrooms, New_baths, New_sqft]])[0]))


for i,prop in enumerate(propsVentas):
    print("calculating rentabillity for each prop" + str(i) + "/" + str(largoVentas))
    rentabilidad = (float(prop[20])*12.0)/(float(prop[2]))
    prop.append(rentabilidad)


print("Sorting by rentabillity")
propsVentas.sort(key=lambda x: float(x[21]))

propsVentas.reverse()

print("Cleaning data and preparing csv")
cleanedData = [["id","precioVenta","dormitorios","banos","mt2","lat","lon","link","arriendoProyectado","rentabilidad"]]
for p in propsVentas:
    newList = []
    newList.append(p[0])
    newList.append(p[2])
    newList.append(p[3])
    newList.append(p[4])
    newList.append(p[6])
    newList.append(p[7])
    newList.append(p[8])
    newList.append(p[14])
    newList.append(p[20])
    newList.append(float(p[21]))
    cleanedData.append(newList)

print("writing csv")
cvsW.writeCsv("dataOrdenadaLimpia.csv", cleanedData)

print(str(datetime.datetime.now().time()))