
#EXTERNAL
import pymysql as mysql
from sklearn import ensemble
from datetime import datetime, timedelta

#INTERNAL
import botPropertyDataBase as db
import fichav2 as ficha
import reportesHuberV1 as reportes
import uf
import pdfCreatorTasacionFull as pdfc
import sendmail


#VALUE SETTING
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)
ufn=uf.getUf()


def obtenerLinks(client,tasacion,venta):

    if "bodegas" not in client:
        client["bodegas"]=0
    if "estacionamientos" not in client:
        client["estacionamientos"]=0
    if "baños" not in client:
        client["baños"]=0
    if "dormitorios" not in client:
        client["dormitorios"]=0
    comuna=client["comuna"]
    if comuna=="Santiago Centro":
        comuna="Santiago"
    precio = int(tasacion[0])
    dormitoriosmin = int(client["dormitorios"])
    dormitoriosmax = int(client["dormitorios"])
    banosmin = int(client["baños"])
    banosmax = int(client["baños"])
    metros = int(client["metros"])
    total = int(client["total"])
    lat = float(client["lat"])
    lon = float(client["lon"])
    estacionamientos = int(client["estacionamientos"])
    bodegas=int(client["bodegas"])
    tipo = client["tipo"]
    region=client["region"]
    if venta:
        operacion="venta"
    else:
        operacion="arriendo"

    flexPrice=[0.05,0.1,0.15,0.2,0.25]
    flexDist=[500,1000,1500,2000,5000]
    flexOther=[False,True]
    props=[]
    for bath in flexOther:
        if bath:
            banosmin=0
            banosmax=10

            dormitoriosmin=0
            dormitoriosmax=10
        for est in flexOther:
            if est:
                estacionamientos=0
                bodegas=0
            for k in flexDist:

                distancia=k

                latmin = lat - ((0.009 / 1000) * distancia)
                latmax = lat + ((0.009 / 1000) * distancia)
                lonmin = lon - ((0.01 / 1000) * distancia)
                lonmax = lon + ((0.01 / 1000) * distancia)

                for j in flexPrice:
                    utilmin = metros * (1 - j)
                    utilmax = metros * (1 + j)
                    totalmin = total * (1 - j)
                    totalmax = total * (1 + j)

                    preciomin=precio*(1-j)
                    preciomax = precio * (1 + j)
                    propsP=reportes.from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,
                                                                   utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,
                                                                   lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,
                                                                   estacionamientos,bodegas,tipo,operacion,region,comuna,
                                                                   'asdfas','asdfas','asdfas','asdfas','asdfas',False)
                    propsY=reportes.from_yapo_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,
                                                                   lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,
                                                                   estacionamientos,bodegas,tipo,operacion,region,comuna,
                                                                   'asdfas','asdfas','asdfas','asdfas','asdfas',False)
                    props=propsP+propsY
                    props=list(props)
                    props.sort(key=lambda x: x[5])
                    for i,prop in enumerate(props):
                        if i>0:
                            if prop[5]==props[(i-1)][5]:
                                props.pop((i-1))
                    if len(props) > 4:
                        break

                if len(props) > 4:
                    break
            if len(props) > 4:
                break
        if len(props) > 4:
            break

    links=[]
    m2=2*precio/(metros+total)
    props2=[]
    for prop in props:
        m2b=(int(20*prop[5]/(prop[8]+prop[9])))/10
        props2.append([prop[14],abs(m2-m2b)])

    props2.sort(key=lambda x:x[1])

    for prop in props2:

        links.append(prop[0])
        if len(links)>9:
            break
    return links


def obtenerIdConLink(link,sitio):

    if (sitio=='www.portalinmobiliario.com'):
        return str(link.split('/')[-1].split('-')[0])
        # mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        # cur = mariadb_connection.cursor()
        # sql = "SELECT id2 from portalinmobiliario WHERE link like '%"+str(link)+"%'"
    else:
        return link.split('.')[2].split('_')[-1]


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
        if len(client["comuna"])>1:
            for comuna in client["comuna"]:
                try:
                    direccion=client["Center"]+", "+comuna+", Chile"
                    break
                except:
                    pass
        else:
            direccion = client["Center"] + ", " + client["comuna"] + ", Chile"
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
                                    None,None,direccion,radiodireccion,corredor,None,True,True)
    if result is not True:
        sendMessageFunc(chat_id,result)
    else:
        sendMessageFunc(chat_id,reply)
        db.insertreporte(client)


def connectorFicha(client):

    if not client["fichafinanciera"]:
        if client["fichapro"] and client["fichainterna"]:
            tipoficha=4
        elif client["fichapro"] and not client["fichainterna"]:
            tipoficha=2
        elif not client["fichapro"] and client["fichainterna"]:
            tipoficha=3
        else:
            tipoficha=1
    else:
        if client["fichapro"] and client["fichainterna"]:
            tipoficha=8
        elif client["fichapro"] and not client["fichainterna"]:
            tipoficha=6
        elif not client["fichapro"] and client["fichainterna"]:
            tipoficha=8
        else:
            tipoficha=6

    if "id_prop" in client:
        text=ficha.crearFicha(client["sitio"],client["id_prop"],client["mail"],tipoficha)
        return text
    else:
        auxlink = str(client["link_prop"])

        # if "https" in auxlink and client["sitio"]=="www.portalinmobiliario.com":
        #     print(auxlink)
        #     auxlink= auxlink.replace('https','http')
        auxlink=auxlink.split('?')
        auxlink=auxlink[0]
        if "//m." in auxlink:
            auxlink=auxlink.replace("//m.","//www.")
        print(auxlink)
        auxid=obtenerIdConLink(auxlink,client["sitio"])

        if len(auxid)==0:
            return "La propiedad buscada no se encuentra en la base de datos"
        else:
            text = ficha.crearFicha(client["sitio"], auxid, client["mail"], tipoficha)
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
    if comuna=="Santiago Centro":
        comuna="Santiago"
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
        if client["tipo"].lower()=="comercial":
            del row[7]
            del row[6]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    # x_train , x_test , y_train , y_test = train_test_split(trainingV , preciosV , test_size = 0.10,random_state = 2)
    #
    # #obtain scores venta:
    # clfHV.fit(x_train, y_train)
    # print("-----------")
    # print("Score Huber:")
    # print(clfHV.score(x_test,y_test))
    # scoreV=clfHV.score(x_test,y_test)

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
        if client["tipo"].lower()=="comercial":
            del row[7]
            del row[6]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    # x_train , x_test , y_train , y_test = train_test_split(trainingA , preciosA , test_size = 0.10,random_state = 2)
    #
    # #obtain scores arriendo:
    # clfHA.fit(x_train, y_train)
    # print("-----------")
    # print("Score Huber:")
    # print(clfHA.score(x_test,y_test))
    # scoreA=clfHA.score(x_test,y_test)

    clfHA.fit(trainingA, preciosA)

    textmail+="Resultados comuna "+str(comuna)+":\nPrecio m2 Venta: UF "+'{:,}'.format((int(10*(m2V/ufn)))/10).replace(",",".")+"\nPrecio m2 Arriendo: $ "+'{:,}'.format(int(m2A)).replace(",",".")+"\n\n"

    ufventacomuna='{:,}'.format((int(10*(m2V/ufn)))/10).replace(",",".")
    arriendocomuna='{:,}'.format(int(m2A)).replace(",",".")


    if client["tipo"].lower()=="comercial":
        tasacionVenta = clfHV.predict([[ int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])
        tasacionArriendo = clfHA.predict([[int(client["baños"]), int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])
    else:
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
        print("precio de arriendo es de: "+str(precioA))

        if client["tipotasacion"]=="Full":

            linksVenta=obtenerLinks(client,precioV,True)
            linksArriendo=obtenerLinks(client,precioA,False)

            print("links obtenidos")

            fileName = "Tasacion " + client["tipo"] + " en " + client["comuna"] + ", " + client[
                "region"] + " cliente " + client["firstname"] + " " + client["lastname"]+".pdf"
            pdfc.crearPdfTasacion(client,precioV,precioA,linksVenta,linksArriendo,fileName,ufventacomuna,arriendocomuna)
            print("pdf creado")
            print(client["mail"],client["firstname"]+" "+client["lastname"],fileName)
            sendmail.sendMail(client["mail"],client["firstname"]+" "+client["lastname"],fileName)
            print('mandando correo con tasacion')

        textmail+="Su propiedad se ha tasado a un valor de venta de UF "+'{:,}'.format(int(precioV/ufn)).replace(",",".")+"\n"
        textmail+="Su propiedad se ha tasado a un valor de arriendo de $ "+'{:,}'.format(int(precioA)).replace(",",".")+"\n"

        print("Texto Full, Check")

        return textmail

### FUCIONES CRM

def buscar(client):

    if client["moneda"]=="UF":
        uf=True
    else:
        uf=False
    if client["metrosmin"] is None:
        client["metrosmin"]=0
    if client["metrosmax"] is None:
        client["metrosmax"]=999999
    if client["totalmin"] is None:
        client["totalmin"]=0
    if client["totalmax"] is None:
        client["totalmax"]=999999
    if client["preciomin"] is None:
        client["preciomin"]=0
    if client["preciomax"] is None:
        client["preciomax"]=99999999999999999999999999999999999999999999999
    print(client)

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='CRM')
    cur = mariadb_connection.cursor()
    if uf:
        sql = "SELECT * FROM propiedades WHERE operacion='" + str(client["operacion"]) + "' AND region='" + str(client["region"]) + "' AND " \
          "comuna='" + str(client["comuna"]) + "' AND tipo='" + str(client["tipo"]) + "' AND dormitorios=" + str(client["dormitorios"]) + " AND " \
          "banos=" + str(client["baños"]) + " AND uf>=" + str(client["preciomin"]*0.95) + " AND uf<=" + str(client["preciomax"]*1.05) + " AND metros>=" + str(client["metrosmin"]) + " AND " \
          "metros<=" + str(client["metrosmax"]) + " AND totales>=" + str(client["totalmin"]) + " AND totales<=" + str(client["totalmax"])

        sql2 = "SELECT * FROM propiedades WHERE operacion='" + str(client["operacion"]) + "' AND region='" + str(
            client["region"]) + "' AND " \
                                "comuna='" + str(client["comuna"]) + "' AND tipo='" + str(
            client["tipo"]) + "' AND dormitorios=" + str(client["dormitorios"]) + " AND " \
                                                                                  "banos=" + str(
            client["baños"]) + " AND pesos>=" + str(client["preciomin"]*ufn*0.95) + " AND pesos<=" + str(
            client["preciomax"]*ufn*1.05) + " AND metros>=" + str(client["metrosmin"]) + " AND " \
                                                                                "metros<=" + str(
            client["metrosmax"]) + " AND totales>=" + str(client["totalmin"]) + " AND totales<=" + str(
            client["totalmax"])
    else:
        sql = "SELECT * FROM propiedades WHERE operacion='" + str(client["operacion"]) + "' AND region='" + str(
            client["region"]) + "' AND " \
                                "comuna='" + str(client["comuna"]) + "' AND tipo='" + str(
            client["tipo"]) + "' AND dormitorios=" + str(client["dormitorios"]) + " AND " \
                                                                                  "banos=" + str(
            client["baños"]) + " AND uf>=" + str(client["preciomin"]*0.95/ufn) + " AND uf<=" + str(
            client["preciomax"]*1.05/ufn) + " AND metros>=" + str(client["metrosmin"]) + " AND " \
                                                                                "metros<=" + str(
            client["metrosmax"]) + " AND totales>=" + str(client["totalmin"]) + " AND totales<=" + str(
            client["totalmax"])

        sql2 = "SELECT * FROM propiedades WHERE operacion='" + str(client["operacion"]) + "' AND region='" + str(
            client["region"]) + "' AND " \
                                "comuna='" + str(client["comuna"]) + "' AND tipo='" + str(
            client["tipo"]) + "' AND dormitorios=" + str(client["dormitorios"]) + " AND " \
                                                                                  "banos=" + str(
            client["baños"]) + " AND pesos>=" + str(client["preciomin"]*0.95) + " AND pesos<=" + str(
            client["preciomax"]*1.05) + " AND metros>=" + str(client["metrosmin"]) + " AND " \
                                                                                      "metros<=" + str(
            client["metrosmax"]) + " AND totales>=" + str(client["totalmin"]) + " AND totales<=" + str(
            client["totalmax"])
    try:
        cur.execute(sql)
    except:
        cur.execute(sql2)

    if client["tipo"]=="Casa":
        supmin="Sup. Construida: "
        supmax="Sup. Terreno: "
    else:
        supmin = "Sup. Útil: "
        supmax = "Sup. Total: "

    props = cur.fetchall()
    mariadb_connection.close()
    tags=["ID: ","Tipo: ","Operación: ", "Región: ","Comuna: ","Dirección","Precio UF: ","Precio (Pesos): ", supmin,supmax,"Dormitorios: ", "Baños: ", "Estacionamientos: ", "Bodegas: ", "Telefono: ","Mail: ",
          "Link Portal: ", "Link Yapo: ", "Comisión: ", "Canje: "]
    text=""
    if len(props) > 0:
        n=0
        for prop in props:
            text += str(n+1)+"\n"
            n+=1
            for x,p in enumerate(prop):
                if p is not None:
                    text+=tags[x]+str(p)+"\n"
            text+="\n"


        return text
    else:
        text="No hay propiedades en el CRM con los criterios elegidos"
    return text

def listaCompleta(client):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='CRM')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM propiedades WHERE operacion='" + str(client["operacion"]) + "' AND region='" + str(
        client["region"]) + "' AND comuna='" + str(client["comuna"]) + "' AND tipo='" + str(client["tipo"])
    cur.execute(sql)


    if client["tipo"] == "Casa":
        supmin = "Sup. Construida: "
        supmax = "Sup. Terreno: "
    else:
        supmin = "Sup. Útil: "
        supmax = "Sup. Total: "

    props = cur.fetchall()
    mariadb_connection.close()
    tags = ["ID: ", "Tipo: ", "Operación: ", "Región: ", "Comuna: ", "Dirección" ,"Precio UF: ", "Precio (Pesos): ", supmin, supmax,
            "Dormitorios: ", "Baños: ", "Estacionamientos: ", "Bodegas: ", "Telefono: ", "Mail: ",
            "Link Portal: ", "Link Yapo: ", "Comisión: ", "Canje: "]
    text = ""
    if len(props) > 0:
        n = 0
        for prop in props:
            text += str(n + 1) + "\n"
            n += 1
            for x, p in enumerate(prop):
                if p is not None:
                    text += tags[x] + str(p) + "\n"
            text += "\n"

        return text
    else:
        text = "No hay propiedades en el CRM con los criterios elegidos"
    return text

def nueva(client):

    try:
        if client["moneda"]=="UF":
            precio=[client["preciomin"],0]
        else:
            precio = [0,client["preciomin"]]
        # 'id': 9561926, 'mail': 'sergei.schkolnik@gmail.com', 'firstname': 'Sergei', 'lastname': 'Schkolnik', 'product': 'CRM', 'crm': 'Nueva',
        # 'tipotasacion': 'Venta', 'region': 'Metropolitana', 'comuna': 'Las Condes', 'tipo': 'Departamento', 'dormitorios': '2', 'baños': '1',
        # 'estacionamientos': '0', 'bodegas': '0', 'metros': 30, 'total': 35, 'adress': 'Guvf', 'moneda': 'UF', 'preciomin': 500, 'telefono': 'Tv',
        # 'mailcliente': 'U', 'linkPortal': 'G', 'linkYapo': 'G', 'comision': 'G'}

        sql = "INSERT INTO propiedades(tipo,operacion,region,comuna,direccion,uf,pesos,metros,totales,dormitorios,banos,estacionamientos," \
              "bodegas,telefono,mail,linkportal,linkyapo,comision,canje) " \
              "VALUES('" + str(client["tipo"]) + "','" + str(client["tipotasacion"]) + "','" + str(client["region"]) + "','" + str(client["comuna"]) + "','" + \
              str(client["adress"]) + "','" + str(precio[0]) + "','" + str(precio[1]) + "','" + str(client["metros"]) + "','" + str(client["total"]) + "','" + \
              str(client["dormitorios"]) + "','" + str(client["baños"]) + "','" + str(client["estacionamientos"]) + "','" + str(client["bodegas"]) + "','" + \
              str(client["telefono"]) + "','" + str(client["mailcliente"]) + "','" + str(client["linkPortal"]) + "','" + str(client["linkYapo"]) + "','" + \
              str(client["comision"]) + "','" + str(client["canje"]) + "')"
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='CRM')
        cur = mariadb_connection.cursor()
        cur.execute(sql)
        mariadb_connection.commit()
        mariadb_connection.close()
        text = "Propiedad Insertada con éxito"
    except Exception as E:
        print(E)
        text="No se pudo insertar la propiedad"
    return text

def selectOne(client):
    if "link_prop" in client:
        client["id_prop"] = obtenerIdConLink(client["link_prop"], client["sitio"])
    if "portal" in client["sitio"]:
        link="linkPortal"
    else:
        link="linkYapo"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='CRM')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM propiedades WHERE "+str(link)+" like'%" + str(client["id_prop"]) + "%'"
    cur.execute(sql)

    prop = cur.fetchall()
    prop = prop[0]
    return prop

def actualizar(client):
    update=client['update'][0]
    if 'tipotasacion' in client:
        client['operacion']=client['tipotasacion']
    if update=='baños':
        client['banos']=client['baños']
        update='banos'
    if "link_prop" in client:
        client["id_prop"] = obtenerIdConLink(client["link_prop"], client["sitio"])
    if "portal" in client["sitio"]:
        link = "linkPortal"
    else:
        link = "linkYapo"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='CRM')
    cur = mariadb_connection.cursor()
    sql = "UPDATE propiedades SET "+str(update)+"='"+str(client[update])+"' WHERE " + str(link) + " like'%" + str(client["id_prop"]) + "%'"
    print(sql)
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()
    text= "Se ha modificado "+str(update)+" a "+str(client[update])+". "

    return text


def eliminar(client):
    text = "Falta Construir Conector de Eliminar"
    return text


