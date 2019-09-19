import tasadorv2
import reportes
import uf
import random

tipo="departamento"

comunas=['']
count=0
deltaprice=[]

data=reportes.from_portalinmobiliario(tipo,"metropolitana",comunas,False)
datalen=len(data)
data=random.shuffle(data)

for prop in data[:100]:
    count+=1
    precio,confianza,nrProps,links,venta,g = tasadorv2.calcularTasacionData(prop[3],prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[8],data)
    realprice=prop[5]/uf.getUf()
    difprice=abs(realprice-precio)/realprice
    deltaprice.append(difprice)
    difpriceprint=int(difprice*100)
    print(str(count)+"/"+str(100)+"----------"+str(difpriceprint)+"% ----------- Realprice: "+str(realprice)+" PredictedPrice: "+str(precio))
print(sum(deltaprice)/len(deltaprice))