import tasadorv2
import reportes
import uf
import random
ufn=uf.getUf()
tipo="departamento"

comunas=['las condes']
count=0
deltaprice=[]

data=reportes.from_portalinmobiliario(tipo,"metropolitana",comunas,False)
datalen=len(data)


for prop in data:
    count+=1
    #print(prop[3], prop[4], prop[10], prop[11], prop[8], prop[9], prop[6], prop[7], prop[12])
    precio,confianza,nrProps,links,venta,g = tasadorv2.calcularTasacionData(prop[3],prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],data)
    #print(precio)
    realprice=prop[5]/ufn
    difprice=abs(realprice-precio)/realprice
    array=[]
    array.append(difprice)
    array.append(nrProps)
    array.append(confianza)
    deltaprice.append(array)
    difpriceprint=int(difprice*100)
    #print(str(count)+"/"+str(100)+"----------"+str(difpriceprint)+"% ----------- Realprice: "+str(realprice)+" PredictedPrice: "+str(precio))
    if count>199:
        break
#print(sum(deltaprice)/len(deltaprice))
deltaprice=sorted(deltaprice, key=lambda x:x[0],reverse=True)

count=0
for i in deltaprice:
    print(i)
    count+=1
    if count<30:
        break
