import botPropertyDataBase as db
import botPropertySelect
import botPropertyMain
import botPropertySelect
import fichav2 as ficha
import reportesHuberV1 as reportes
import pymysql as mysql
import uf
import tasadorbot2 as tb2
#import tasadorbot2 as tb2
ufn=uf.getUf()
from sklearn import ensemble
from sklearn.model_selection import train_test_split
import reportesHuberV1 as reportes


def obtenerIdConLink(link,sitio):

    if (sitio=='www.portalinmobiliario.com'):
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        sql = "SELECT id2 from portalinmobiliario WHERE link like '%"+str(link)+"%'"
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT id2 from propiedades WHERE link like '%"+str(link)+"%'"
    cur.execute(sql)
    id = cur.fetchall()
    if len(id)>0:
        return id[0]
    else:
        return id


def generarreporte(client,sendMessageFunc,chat_id,reply):
    if client["moneda"]=="UF" and client["preciomin"] is not None:
        client["preciomin"]=client["preciomin"]*ufn
        client["preciomax"]=client["preciomax"]*ufn
    client["tipo"]= client["tipo"].lower()
    client["operacion"]= client["operacion"].lower()
    if client["operacion"]=="comprar":
        client["operacion"]= "venta"
    else:
        client["operacion"]= "arriendo"

    if client["preciomin"] is None:
        client["preciomin"]=0
        client["preciomax"]=999999999999
    if client["metrosmin"] is None:
        client["metrosmin"]=0
        client["metrosmax"]=99999999
        client["totalmin"]=0
        client["totalmax"]=99999999

    if "totalmin" not in client:
        client["totalmin"]=0
        client["totalmax"]=99999999

    if "DormMin" in client and "DormMax" in client:
        dormitoriosmin = client["DormMin"]
        dormitoriosmax = client["DormMax"]

    elif "dormitorios" in client:
        if client["dormitorios"]=='4+':
            dormitoriosmin=4
            dormitoriosmax=None
        elif client["dormitorios"] is None:
            dormitoriosmin = None
            dormitoriosmax = None
        else:
            dormitoriosmin=client["dormitorios"]
            dormitoriosmax=client["dormitorios"]
    else:
        dormitoriosmin=None
        dormitoriosmax=None

    if "BathMin" in client and "BathMax" in client:
        banosmin = client["BathMin"]
        banosmax = client["BathMax"]

    elif "baños" in client:
        if client["baños"]=='4+':
            banosmin=4
            banosmax=None
        elif client["baños"] is None:
            banosmin = None
            banosmax = None
        else:
            banosmin=client["baños"]
            banosmax=client["baños"]
    else:
        banosmin = None
        banosmax = None
    if "estacionamientos" not in client:
        client["estacionamientos"]=0


    if client["reportepro"]:
        confmin=13
        rentminventa=-0.8
        rentminarriendo=0.01
    else:
        confmin=None
        rentminventa=None
        rentminarriendo=None
    if client["reporteinterno"]:
        corredor="0"
    else:
        corredor=None
    if not client["reportemetro"]:
        metrodistance=None
    else:
        metrodistance=99999
    if client["comuna"]=="Santiago Centro":
        client["comuna"]="santiago"

    if "Center" in client and "Radius" in client:
        direccion=client["Center"]
        radiodireccion=client["Radius"]
    else:
        direccion = None
        radiodireccion = None

    listaComunas=[]
    if type(client["comuna"]) is list:
        for comuna in client["comuna"]:
            listaComunas.append(comuna.lower())
    else:
        listaComunas.append(client["comuna"].lower())

    result=reportes.generarReporteSeparado(client["preciomin"],client["preciomax"],client["metrosmin"],client["metrosmax"],client["totalmin"],client["totalmax"],
                                    None,None, None,None,dormitoriosmin,dormitoriosmax, banosmin, banosmax,
                                    confmin, rentminventa, rentminarriendo,None, None, metrodistance, None, None, None, client["tipo"], client["operacion"],
                                    client["region"].lower(),listaComunas, None, client["mail"],(client["firstname"]+" "+client["lastname"]),
                                    None,None,direccion,radiodireccion,corredor,None,True)
    if result is not True:
        sendMessageFunc(chat_id,result)
    else:
        sendMessageFunc(chat_id,reply)
        db.insertreporte(client)



def connectorFicha(client):

    if client["fichapro"] and client["fichainterna"]:
        tipoficha=4
    elif client["fichapro"] and not client["fichainterna"]:
        tipoficha=2
    elif not client["fichapro"] and client["fichainterna"]:
        tipoficha=3
    else:
        tipoficha=1

    if "id_prop" in client:
        text=ficha.crearFicha(client["sitio"],client["id_prop"],client["mail"],tipoficha)
        return text
    else:
        auxlink = str(client["link_prop"])
        if "https" in auxlink and client["sitio"]=="www.portalinmobiliario.com":
            print(auxlink)
            auxlink= auxlink.replace('https','http')
        auxlink=auxlink.split('?')
        auxlink=auxlink[0]
        if "//m." in auxlink:
            auxlink=auxlink.replace("//m.","//www.")
        print(auxlink)
        auxid=obtenerIdConLink(auxlink,client["sitio"])

        if len(auxid)==0:
            return "La propiedad buscada no se encuentra en la base de datos"
        else:
            print(auxid[0])
            text = ficha.crearFicha(client["sitio"], auxid[0], client["mail"], tipoficha)
            return text

def tasador(client):


    textmail=""
    regionYapoAux=client["region"]
    regYapoDict={
        "Metropolitana":"15",
        "Valparaiso":"6",
        "Valparaíso":"6",
        "Arica":"1",
        "Iquique":"2",
        "Antofagasta":"3",
        "Atacama":"4",
        "Coquimbo":"5",
        "Ohiggins":"7",
        "Maule":"8",
        "Ñuble":"16",
        "Biobio":"9",
        "Araucania":"10",
        "Los Rios":"11",
        "Los Lagos":"12",
        "Aysen":"13",
        "Magallanes":"14",

    }
    regionYapo=regYapoDict[regionYapoAux]

    print("Diccionario de Regiones para Yapo Creado")

    if "bodegas" not in client:
        client["bodegas"]=0
    if "estacionamientos" not in client:
        client["estacionamientos"]=0
    if "baños" not in client:
        client["baños"]=0
    if "dormitorios" not in client:
        client["dormitorios"]=0
    comuna=client["comuna"]
    listacomunas=[]
    listacomunas.append(comuna)


    propsPV = reportes.from_portalinmobiliario(client["tipo"].lower(),client["region"].lower(),listacomunas,"venta",True)
    propsYV = reportes.from_yapo(client["tipo"].lower(),regionYapo,listacomunas,True,"venta",True)
    propsV = propsPV + propsYV
    # aca deberiamos hacer el GB

    m2=reportes.m2prom(client["tipo"].lower(),comuna,client["region"].lower())
    m2V=m2[0]
    m2A=m2[1]

    clfHV = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                              learning_rate=0.1, loss='huber')

    #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

    preciosV = [row[5] for row in propsV]

    trainingV = propsV.copy()
    for row in trainingV:
        del row[13]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    x_train , x_test , y_train , y_test = train_test_split(trainingV , preciosV , test_size = 0.10,random_state = 2)

    #obtain scores venta:
    clfHV.fit(x_train, y_train)
    print("-----------")
    print("Score Huber:")
    print(clfHV.score(x_test,y_test))
    scoreV=clfHV.score(x_test,y_test)

    clfHV.fit(trainingV, preciosV)

    propsPA = reportes.from_portalinmobiliario(client["tipo"].lower(),client["region"].lower(),listacomunas,"arriendo",True)
    propsYA = reportes.from_yapo(client["tipo"].lower(),regionYapo,listacomunas,True,"arriendo",True)
    propsA = propsPA + propsYA
    # aca deberiamos hacer el GB

    clfHA = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                              learning_rate=0.1, loss='huber')

    #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

    preciosA = [row[5] for row in propsA]

    trainingA = propsA.copy()
    for row in trainingA:
        del row[13]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    x_train , x_test , y_train , y_test = train_test_split(trainingA , preciosA , test_size = 0.10,random_state = 2)

    #obtain scores arriendo:
    clfHA.fit(x_train, y_train)
    print("-----------")
    print("Score Huber:")
    print(clfHA.score(x_test,y_test))
    scoreA=clfHA.score(x_test,y_test)

    clfHA.fit(trainingA, preciosA)

    textmail+="Resultados comuna "+str(comuna)+":\n"+"Score Ventas: "+str((int(10000*scoreV))/100)+"%\nScore Arriendos: "+str((int(10000*scoreA))/100)+"%\nPrecio m2 Venta: UF "+'{:,}'.format((int(10*(m2V/ufn)))/10).replace(",",".")+"\nPrecio m2 Arriendo: $ "+'{:,}'.format(int(m2A)).replace(",",".")+"\n\n"
    tasacionVenta = clfHV.predict([[int(client["dormitorios"]),int(client["baños"]), int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])
    tasacionArriendo = clfHA.predict([[int(client["dormitorios"]),int(client["baños"]), int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])

    precioV = tasacionVenta
    precioA = tasacionArriendo


    print("Tasacion Check")

    if precioV==None:
        text="No se ha podido realizar la tasación."
        return text
    else:
        print("precio de venta es de: "+str(precioV))
        print("precio de venta es de: "+str(precioA))


        textmail+="Su propiedad se ha tasado a un valor de venta de UF "+'{:,}'.format(int(precioV/ufn)).replace(",",".")+"\n"
        textmail+="Su propiedad se ha tasado a un valor de arriendo de $ "+'{:,}'.format(int(precioA)).replace(",",".")+"\n"

        print("Texto Full, Check")
        return textmail
