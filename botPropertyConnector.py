import botPropertyDataBase
import botPropertySelect
import botPropertyMain
import botPropertySelect
import ficha
import reportes
import pymysql as mysql
import uf
import tasadorbot2 as tb2
ufn=uf.getUf()

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

def generarreporte(client):
    if client["moneda"]=="UF":
        client["preciomin"]=client["preciomin"]*ufn
        client["preciomax"]=client["preciomax"]*ufn
    client["tipo"]= client["tipo"].lower()
    client["operacion"]= client["operacion"].lower()
    if client["operacion"]=="comprar":
        client["operacion"]= "venta"
    else:
        client["operacion"]= "arriendo"
    listaComunas=[]
    listaComunas.append(client["comuna"].lower())

    if client["dormitorios"]=='4+':
        dormitoriosmin=4
        dormitoriosmax=None
    else:
        dormitoriosmin=client["dormitorios"]
        dormitoriosmax=client["dormitorios"]

    if client["baños"]=='4+':
        banosmin=4
        banosmax=None
    else:
        banosmin=client["baños"]
        banosmax=client["baños"]

    reportes.generarReporteSeparado(client["preciomin"],client["preciomax"],client["metrosmin"],client["metrosmax"],client["totalmin"],client["totalmax"],
                                    None,None, None,None,dormitoriosmin,dormitoriosmax, banosmin, banosmax,
                                    None, None, None,None, None, None, None, None, None, client["tipo"], client["operacion"],
                                    client["region"].lower(),listaComunas, None, client["mail"],(client["firstname"]+" "+client["lastname"]),
                                    None,None,None,None,None,None,True)

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

    confDict={
        "AA+":"98%",
        "AA-":"95%",
        "A+":"90%",
        "A-":"85%",
        "B+":"80%",
        "B-":"70%",
        "C+":"60%",
        "C-":"50%",
        "D+":"30%",
        "D-":"10%",
        "E":"0%",
    }
    print("Diccionario de Confianza Creado")

    regYapoDict={
        "Metropolitana":"15",
        "Valparaiso":"6",
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
    print("Diccionario de Regiones para Yapo Creado")

    propsP=reportes.from_portalinmobiliario(client["tipo"].lower(),client["region"].lower(),True)
    propsY=reportes.from_yapo(client["tipo"].lower(),regYapoDict[client["region"]],True,True)
    props=propsP+propsY
    print("Propiedades Check")

    tasacion=tb2.calcularTasacionData(client["operacion"].lower(),client["tipo"].lower(),client["lat"],client["lon"],int(client["metros"]),
                                      int(client["total"]),int(client["dormitorios"]),int(client["baños"]),int(client["estacionamientos"]),props)
    print("Tasacion Check")

    if tasacion[0]==None:
        text="No se ha podido realizar la tasación."
        return text
    else:
        if tasacion[4]:
            text="La propiedad ha sido comparada con las siguientes propiedades (entre otras):"
            print("Texto inicial Check")
            links=tasacion[3][:5]
            print("reducción de links, check")
            for link in links:
                text+='\n'
                text+=link
            text+='\n'
            text+="Su propiedad se ha tasado a un valor de venta de UF. "+'{:,}'.format(tasacion[0]).replace(",",".")+" ,con una confianza de: "+confDict[tasacion[1]]+"."

            print("Texto Full, Check")
            return text
        else:
            text="La propiedad ha sido comparada con las siguientes propiedades (entre otras):"
            print("Texto inicial Check")
            links=tasacion[3][:5]
            print("reducción de links, check")
            for link in links:
                text+='\n'
                text+=link
            text+='\n'
            text+="Su propiedad se ha tasado a un valor arriendo de $ "+'{:,}'.format(tasacion[0]).replace(",",".")+" ,con una confianza de: "+confDict[tasacion[1]]+"."

            print("Texto Full, Check")
            return text
