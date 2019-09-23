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

ponds=[0.1,0.5,1,1.5,2,2.5,5,10]
results=[]

for pd in ponds:
    for prop in data:
        count+=1
        #print(prop[3], prop[4], prop[10], prop[11], prop[8], prop[9], prop[6], prop[7], prop[12])
        precio,confianza,nrProps,links,venta,g = tasadorv2.calcularTasacionData(prop[3],prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],data,pd)
        #print(precio)
        realprice=prop[5]/ufn
        difprice=abs(realprice-precio)/realprice
        array=[]
        array.append(difprice)
        array.append(nrProps)
        array.append(confianza)
        deltaprice.append(array)
        difpriceprint=int(difprice*100)
        print(str(count)+"/"+str(100)+"----------"+str(difpriceprint)+"% ----------- Realprice: "+str(realprice)+" PredictedPrice: "+str(precio))
        # print(nrProps)
        # print(confianza)
        if count>100:
            break
    #print(sum(deltaprice)/len(deltaprice))
    deltaprice=sorted(deltaprice, key=lambda x:x[0],reverse=True)

    count=0
    total=0
    for i in deltaprice:
        if i<1:
            total+=i[0]
            count+=1
    results.append(total/count)
for res in results:
    print("avg: "+str(res))
