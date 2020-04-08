
#EXTERNAL
import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta
import datetime
import requests
from sklearn import ensemble
from sklearn.model_selection import train_test_split
import time
import random
from lxml import html
import os

#INTERNAL
import indicadoresV3 as indicadores
import sendMailV3
import pubPortalExiste
from xlsxWriterV3 import writeXlsx
import googleMapApi as gm
import headersV3 as headers

#VALUES SETTING:
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=30)
yesterday=datetime.date(yesterday)
fechahoy = datetime.datetime.now()
fechahoy=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)


def esDueno(link):
    headerIndex = 0
    headerList=headers.headerList
    try:
        request = requests.get(link, headers=headerList[headerIndex])
    except:
        time.sleep(random.randint(60, 90))
        headerIndex += 1
        request = requests.get(link, headers=headerList[headerIndex])
    try:
        tree = html.fromstring(request.content)
    except:
        return "no"
    agency_path = '//*[@id="real_estate_agency"]'
    agency = tree.xpath(agency_path)
    esPropietario = "no"
    if len(agency) == 0:
        # no hay agency; es dueño.
        esPropietario = "si"

    if "orredor" in request.text:
        esPropietario="no"
    if "omisión" in request.text:
        if "2%" in request.text or "50%" in request.text:
            esPropietario = "no"
        elif "in Comisi" in request.text or "in comisi" in request.text:
            esPropietario="si"
    if esPropietario=="si":
        textoventa = ((request.text).split('Escribe tu pregunta...">')[1]).split("</textarea>")[0]
        if "ropiedad" in textoventa or "orredor" in textoventa or "state" in textoventa or "ome" in textoventa or "nversi" in textoventa:
            esPropietario="no"
    return esPropietario

def m2prom(tipo,comuna,region):
    #Transformar comuna a minúsculas
    comuna=comuna.lower()

    #Obtener Arriendos
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT (2*precio/(metrosmin+metrosmax)) FROM portalinmobiliario WHERE operacion='arriendo' and tipo='"+str(tipo)+"' and link like '%"+str(comuna)+"%' and precio is not NULL AND metrosmin IS NOT NULL AND metrosmax IS NOT NULL AND precio>0 AND metrosmin>0 AND metrosmax>0"
    cur.execute(sql)
    arriendo = cur.fetchall()
    arriendo = sorted(arriendo)
    larriendo = len(arriendo)
    minarriendo = int(larriendo * 0.1)
    maxarriendo = int(larriendo * 0.9)
    arriendo = arriendo[minarriendo:maxarriendo]
    sumarriendo = 0
    for i in arriendo:
        sumarriendo+=i[0]
    promarriendo = (sumarriendo) / max(len(arriendo), 1)

    #Otener Ventas
    cur = mariadb_connection.cursor()
    sql = "SELECT (2*precio/(metrosmin+metrosmax)) FROM portalinmobiliario WHERE operacion='venta' and tipo='"+str(tipo)+"' and link like '%"+str(comuna)+"%' and precio is not NULL AND metrosmin IS NOT NULL AND metrosmax IS NOT NULL AND precio>0 AND metrosmin>0 AND metrosmax>0"
    cur.execute(sql)
    venta = cur.fetchall()
    venta = sorted(venta)
    lventa=len(venta)
    minventa=int(lventa*0.1)
    maxventa=int(lventa*0.9)
    venta=venta[minventa:maxventa]
    sumventa=0
    for j in venta:
        sumventa+=j[0]
    promventa=float(sumventa)/max(len(venta),1)

    try:
        return promventa,promarriendo
    except:
        return 0,0

def estaciones(l1,l2,l3,select):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='metro')
    cur = mariadb_connection.cursor()
    if select:
        sql = "SELECT * FROM estaciones where linea like '%"+str(l1)+"%' or linea like '%"+str(l2)+"%' or linea like '%"+str(l3)+"%'"
    else:
        sql = "SELECT * FROM estaciones"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla


def from_yapo_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,
                                   lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,bodegas,tipo,
                                   operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6,latlonyapo,verboso=False):
        if region=="metropolitana":
            region="15"
        if verboso:
            print("----------------------")
            print("Seleccionando propiedades especificas de yapo.")
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()

        sqlselect = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,preciopesos,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,estacionamientos,link,id,esdueno FROM propiedades WHERE "
        sql=sqlselect

        #clausulas de integridad de datos
        if latlonyapo:
            sqlwhere = "lat!='-999' AND metrosmin!='-1' AND metrosmax!='-1' AND "
            sql = sql + sqlwhere

        sqlwhere="fechascrap>='"+str(yesterday)+"' AND "
        sql=sql+sqlwhere

        sqlwhere="fechapublicacion>='"+str(past)+"' AND "
        sql=sql+sqlwhere

        sqlwhere="preciopesos>="+str(preciomin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="preciopesos<="+str(preciomax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin>="+str(utilmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin<="+str(utilmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax>="+str(totalmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax<="+str(totalmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat>="+str(latmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat<="+str(latmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon>="+str(lonmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon<="+str(lonmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="dormitorios>="+str(dormitoriosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="dormitorios<="+str(dormitoriosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="banos>="+str(banosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="banos<="+str(banosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="estacionamientos>="+str(estacionamientos)+" AND "
        sql=sql+sqlwhere

        sqlwhere="tipo LIKE '%" + str(tipo) + "%' AND "
        sql=sql+sqlwhere

        sqlwhere="operacion LIKE '%"+str(operacion)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="idregion LIKE '%"+str(region)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="(comuna LIKE '%" + comuna1 + "%' or comuna LIKE '%"+ comuna2 + "%' or comuna LIKE '%"+ comuna3 + "%' or comuna LIKE '%"+ comuna4 + "%' or comuna LIKE '%"+ comuna5 +"%' or comuna LIKE '%"+ comuna6 +"%')"
        sql=sql+sqlwhere

        if verboso:
            print("Consulta YAPO:")
            print(sql)
        cur.execute(sql)
        tupla = cur.fetchall()
        if verboso:
            print("Datos de consulta especifica de YAPO listos")
            print("Se han encontrado "+str(len(tupla))+" propiedades.")
            print("----------------------")
        return tupla

def from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,
                                   lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,bodegas,tipo,
                                   operacion,region,comuna,verboso=False):

        comuna=comuna.lower()

        if verboso:
            print("----------------------")
            print("Seleccionando propiedades especificas de portal.")
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()

        sqlselect = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,bodegas,link,id FROM portalinmobiliario WHERE "

        sqlwhere="fechascrap>='"+str(yesterday)+"' AND "
        sql=sqlselect+sqlwhere

        sqlwhere="fechapublicacion>='"+str(past)+"' AND "
        sql=sql+sqlwhere

        sqlwhere="precio>="+str(preciomin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="precio<="+str(preciomax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin>="+str(utilmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin<="+str(utilmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax>="+str(totalmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax<="+str(totalmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat>="+str(latmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat<="+str(latmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon>="+str(lonmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon<="+str(lonmax)+" AND "
        sql=sql+sqlwhere
        if tipo not in 'local comercial':
            sqlwhere="dormitorios>="+str(dormitoriosmin)+" AND "
            sql=sql+sqlwhere

            sqlwhere="dormitorios<="+str(dormitoriosmax)+" AND "
            sql=sql+sqlwhere

            sqlwhere="banos>="+str(banosmin)+" AND "
            sql=sql+sqlwhere

            sqlwhere="banos<="+str(banosmax)+" AND "
            sql=sql+sqlwhere

            sqlwhere="estacionamientos>="+str(estacionamientos)+" AND "
            sql=sql+sqlwhere

            sqlwhere="bodegas>="+str(bodegas)+" AND "

        sql=sql+sqlwhere

        sqlwhere="tipo LIKE '%" + str(tipo) + "%' AND "
        sql=sql+sqlwhere

        sqlwhere="operacion LIKE '%"+str(operacion)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="region LIKE '%"+str(region)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="(comuna LIKE '%" + comuna +"&')"
        sql=sql+sqlwhere

        if verboso:
            print("Consulta:")
            print(sql)
        cur.execute(sql)
        tupla = cur.fetchall()
        if verboso:
            print("Datos de consulta especifica de portal listos")
            print("Se han encontrado "+str(len(tupla))+" propiedades.")
            print("----------------------")
        return tupla

def insertarClientes_Propiedades(resultado):
    sql = """INSERT INTO clientes_propiedades(uni,cliente,prop)
             VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE prop=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (resultado))
    mariadb_connection.commit()
    mariadb_connection.close()

def actualizarActividad(cliente):

    sql = "UPDATE clientes SET activo=2 WHERE id="+str(cliente)

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def precio_from_portalinmobiliario(id2):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio

def from_portalinmobiliario(tipo,region,comunas,op,verboso=False):
    if verboso:
        print("----------------------")
        print("Extrayendo propiedades de region: "+str(region)+" de portalinmobiliario.")
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sqlcomunas=''
    for comuna in comunas:
        comuna=comuna.lower()
        sqlcomunas+="comuna like '%"+str(comuna)+"%' or "
    sqlcomunas=sqlcomunas[:-4]
    if sqlcomunas!='':
        sqlcomunas='('+sqlcomunas+') '
    sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link FROM portalinmobiliario WHERE fechapublicacion>'"+str(past) +"' and operacion='" + op + "' and "+sqlcomunas+"and tipo='"+str(tipo)+"' and region='"+str(region)+"'"
    # if verboso:
    #     print("Consulta: ")
    #     print(sql)
    print(sql)
    cur.execute(sql)
    tupla = cur.fetchall()
    data = []
    for i in tupla:
        subdata=[]
        a=0
        for j in range (0,len(i)):
            if (i[j]==None):
                a=1
            subdata.append(i[j])
        if (a==0):
            data.append(subdata)

    if verboso:
        print("Data de portal Lista.")
        print("Se han encontrado "+str(len(data))+" propiedades.")
        print("----------------------")
    return data

def from_yapo(tipo,region,comunas,latlonyapo,op,verboso=False):
    if region=="metropolitana":
            region="15"
    comuna=comunas[0].lower()

    if verboso:
        print("----------------------")
        print("Extrayendo propiedades de region: "+str(region)+" de yapo.")
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
    cur = mariadb_connection.cursor()
    if latlonyapo:
        sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,preciopesos,dormitorios,banos,metrosmin,metrosmax,lat,lon," \
              "estacionamientos,link FROM propiedades WHERE fechapublicacion>'"+str(past) +"' and operacion='" + op + "' and " \
              "tipo='"+str(tipo)+"' AND idregion='"+str(region)+"' AND lat!='-999' AND metrosmin!='-1' AND metrosmax!='-1'"
    else:
        sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,preciopesos,dormitorios,banos,metrosmin,metrosmax,lat,lon," \
              "estacionamientos,link FROM propiedades WHERE fechapublicacion>'"+str(past) +"' and operacion='" + op + "' and tipo='"+str(tipo)+"'"

    # if verboso:
    #     print("Consulta: ")
    print(sql)
    cur.execute(sql)
    tupla = cur.fetchall()
    data = []
    for i in tupla:
        subdata=[]
        a=0
        for j in range (0,len(i)):
            if (i[j]==None):
                a=1
            subdata.append(i[j])
        if (a==0):
            data.append(subdata)

    if verboso:
        print("Data de Yapo Lista.")
        print("Se han encontrado "+str(len(data))+" propiedades.")
        print("----------------------")
    return data

def main():
    pass

def yaReportadoYapo(idCliente,idProp):
    sql = "SELECT * from clientes_propiedades WHERE cliente =" + str(idCliente) + " and prop=" + str(idProp)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    if len(result) > 0:
        result=result[0]
        fechareporte=result[3]
        return True,fechareporte
    else:
        return False,'2000-01-01'

def yaReportado(idCliente,idProp):
    sql = "SELECT * from clientes_propiedades WHERE cliente =" + str(idCliente) + " and prop=" + str(idProp)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    if len(result) > 0:
        result=result[0]
        fechareporte=result[3]
        return True,fechareporte
    else:
        return False,'2000-01-01'

def guardarRegistro(idCliente,idProp,fechareporte):
    sql = "INSERT INTO clientes_propiedades(cliente,prop,fecha) VALUES('" + str(idCliente) + "','" + str(idProp) + "','" + str(fechareporte) + "') ON DUPLICATE KEY UPDATE prop='" + str(idProp) + "';"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def guardarRegistroYapo(idCliente,idProp,fechareporte):
    sql = "INSERT INTO clientes_propiedades(cliente,prop,fecha) VALUES('" + str(idCliente) + "','" + str(idProp) + "','" + str(fechareporte) + "') ON DUPLICATE KEY UPDATE prop='" + str(idProp) + "';"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def getDatosDueno(idProp2):
    sql = "SELECT mail,telefono,esDueno from duenos WHERE idProp =" + str(idProp2)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    result = result[0]
    return result[0],result[1],result[2]

def crearCarpetaSiNoExiste(nombrecarpetadb,fechahoy,nombreCliente):
    # Create target Directory if don't exist
    path = os.path.join(os.path.expanduser('~'), 'Dropbox', 'Reportes', str(nombrecarpetadb), str(nombreCliente))
    if not os.path.exists(path):
        os.mkdir(path)

    path = os.path.join(os.path.expanduser('~'), 'Dropbox', 'Reportes', str(nombrecarpetadb), str(nombreCliente),str(fechahoy))
    if not os.path.exists(path):
        os.mkdir(path)

def generarReporte(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax, lonmin, lonmax,
                       dormitoriosmin,dormitoriosmax, banosmin, banosmax, rentminventa, rentminarriendo,
                           estacionamientos, bodegas, metrodistance, l1, l2, l3, tipo,operacion, region, listaComunas, prioridad, mail,
                           nombreCliente,nombrecarpetadb,idCliente,direccion,radioDireccion,corredor,topx,verboso,separado):

    uf = indicadores.getUf()
    textmail=""
    columnNames = []
    columnNames.append('Código')
    if preciomin is not None:
        preciomin = float(preciomin)
    else:
        preciomin=0
    columnNames.append("Precio")
    if tipo=="casa":
        columnNames.append("UF/m2 constr.")
        columnNames.append("UF/m2 terren.")
    else:
        columnNames.append("UF/m2")
    if preciomax is not None:
        preciomax = float(preciomax)
    else:
        preciomax=999999999999

    if utilmin is not None:
        utilmin = int(utilmin)
    else:
        utilmin=0
    columnNames.append("Util")

    if utilmax is not None:
        utilmax = int(utilmax)
    else:
        utilmax=99999999

    if totalmin is not None:
        totalmin = int(totalmin)
    else:
        totalmin=0
    columnNames.append("Total")

    columnNames.append("Dorm.")

    columnNames.append("Banos")

    columnNames.append("Estac.")
    columnNames.append("Bod.")
    if totalmax is not None:
        totalmax = int(totalmax)
    else:
        totalmax=99999999

    if latmin is not None:
        latmin = float(latmin)
    else:
        latmin=-9998

    if latmax is not None:
        latmax = float(latmax)
    else:
        latmax=999999

    if lonmin is not None:
        lonmin = float(lonmin)
    else:
        lonmin=-9999999

    if lonmax is not None:
        lonmax = float(lonmax)
    else:
        lonmax=9999999
    if tipo == "oficina":
        if dormitoriosmin is not None:
            dormitoriosmin = int(dormitoriosmin)
        else:
            dormitoriosmin=0

        if dormitoriosmax is not None:
            dormitoriosmax = int(dormitoriosmax)
        else:
            dormitoriosmax=100

        if banosmin is not None:
            banosmin = int(banosmin)
        else:
            banosmin=0

        if banosmax is not None:
            banosmax = int(banosmax)
        else:
            banosmax=100
    elif tipo not in 'local comercial':
        if dormitoriosmin is not None:
            dormitoriosmin = int(dormitoriosmin)
        else:
            dormitoriosmin=1

        if dormitoriosmax is not None:
            dormitoriosmax = int(dormitoriosmax)
        else:
            dormitoriosmax=10

        if banosmin is not None:
            banosmin = int(banosmin)
        else:
            banosmin=1

        if banosmax is not None:
            banosmax = int(banosmax)
        else:
            banosmax=6
    else:
        dormitoriosmin=0
        dormitoriosmax=0
        banosmin=0
        banosmax=0

    if metrodistance is not None:
        metrodistance = int(metrodistance)
        columnNames.append("Metro")
        columnNames.append("Dist metro")


    else:
        metrodistance=999999999

    if rentminventa is not None and operacion=='venta':
        rentminventa = float(rentminventa)
        columnNames.append("Pr. Venta Tasado")
        if tipo=="casa":
            columnNames.append("UF/m2 pred. constr.")
            columnNames.append("UF/m2 pred. terren.")
        else:
            columnNames.append("UF/m2 predicho")

        columnNames.append("Rent. Venta")



    else:
        rentminventa=False

    if corredor is not None:
        corredor=str(corredor)
    else:
        corredor="a"

    if rentminarriendo is not None:
        rentminarriendo = float(rentminarriendo)
        columnNames.append("Pr. Arriendo Tasado")
        columnNames.append("Rent. Arriendo")
    else:
        rentminarriendo=False



    if estacionamientos is not None:
        estacionamientos = int(estacionamientos)
    else:
        estacionamientos=0

    if bodegas is not None:
        bodegas = int(bodegas)
    else:
        bodegas=0

    if tipo is not None:
        tipo = str(tipo)
    else:
        print("Error, debe haber tipo")
        return True


    if operacion is not None:
        operacion = str(operacion)
    else:
        print("Error, debe haber operacion")
        return True

    if region is not None:
        region = str(region)

    else:
        print("Error, debe haber region")
        return True

    if region is not None:
        prioridad = str(prioridad)


    if mail is not None:
        mail = str(mail)
    else:
        print("Error, debe haber mail")
        return True

    if nombreCliente is not None:
        nombreCliente = str(nombreCliente)
    else:
        print("Error, debe haber nombre Cliente")
        return True

    if direccion is not None and radioDireccion is not None:
        direccion = str(direccion)
        distancia = int(radioDireccion)
        latD, lonD = gm.getCoordsWithAdress(direccion)

        latD = float(latD)
        lonD = float(lonD)

        latminD = latD - ((0.009 / 1000) * distancia)
        latmaxD = latD + ((0.009 / 1000) * distancia)
        lonminD = lonD - ((0.01 / 1000) * distancia)
        lonmaxD = lonD + ((0.01 / 1000) * distancia)

        latmin = max(latmin,latminD)
        latmax = min(latmax,latmaxD)
        lonmin = max(lonmin,lonminD)
        lonmax = min(lonmax,lonmaxD)

    if ((l1 is not None) or (l2 is not None) or (l3 is not None)):

        selectEstacion=True
        if l1 is None:
            l1='abcdeFG'
        if l2 is None:
            l2='abcdeFG'
        if l3 is None:
            l3='abcdeFG'
    else:
        selectEstacion = False
    estaciones1=estaciones(l1,l2,l3,selectEstacion)

    if corredor is not None:
        columnNames.append("Link")
        columnNames.append("Mail")
        columnNames.append("Telefono")
        columnNames.append("es dueno")
    columnNames.append('fecha encontrado')

    if rentminventa is not False:
        columnNames.append("Calidad Tasacion Venta")
    if rentminarriendo is not False:
        columnNames.append("Calidad Tasacion Arriendo")
    columnNames.append("Observaciones")
    listaAdjuntos=[]

    if (rentminventa is not False or rentminarriendo is not False):
        latlonyapo=True
    else:
        latlonyapo=False



    for comuna in listaComunas:
        propsPV = from_portalinmobiliario(tipo, region, [comuna], "venta", verboso)
        propsYV = from_yapo(tipo, region, [comuna], latlonyapo, "venta", verboso)
        propsV = propsPV + propsYV
        comuna=comuna.lower()

        if comuna=='santiago centro':
            comuna='santiago'

        m2=m2prom(tipo,comuna,region)
        m2V=m2[0]
        m2A=m2[1]

        clfHV = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                                  learning_rate=0.1, loss='huber')


        #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

        preciosV = [row[5] for row in propsV]

        trainingV = propsV.copy()
        for row in trainingV:
            del row[13]
            if tipo=="comercial":
                del row[7]
                del row[6]
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

        propsPA = from_portalinmobiliario(tipo, region, [comuna], "arriendo", verboso)
        propsYA = from_yapo(tipo, region, [comuna], latlonyapo, "arriendo", verboso)
        propsA = propsPA + propsYA
        # aca deberiamos hacer el GB

        clfHA = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                                  learning_rate=0.1, loss='huber')

        #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

        preciosA = [row[5] for row in propsA]

        trainingA = propsA.copy()
        for row in trainingA:
            del row[13]
            if tipo=="comercial":
                del row[7]
                del row[6]
            del row[5]
            del row[4]
            del row[3]
            del row[2]
            del row[1]
            del row[0]

        x_train , x_test , y_train , y_test = train_test_split(trainingA , preciosA , test_size = 0.10,random_state = 2)
        print(x_train)
        print(y_train)
        #obtain scores arriendo:
        clfHA.fit(x_train, y_train)
        print("-----------")
        print("Score Huber:")
        print(clfHA.score(x_test,y_test))
        scoreA=clfHA.score(x_test,y_test)

        clfHA.fit(trainingA, preciosA)

        textmail+="Resultados comuna "+str(comuna)+":\n"+"Score Ventas: "+str((int(10000*scoreV))/100)+"%\nScore Arriendos: "+str((int(10000*scoreA))/100)+"%\nPrecio m2 Venta: UF."+str((int(10*(m2V/uf)))/10)+"\nPrecio m2 Arriendo: $"+str((int(m2A)))+"\n\n"


        for d in range(dormitoriosmin, dormitoriosmax + 1):
            for b in range(banosmin, banosmax + 1):

                if separado:
                    d2=d
                    b2=b
                else:
                    d2=dormitoriosmax
                    b2=banosmax

                propiedadesP=from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,
                                               latmin,latmax,lonmin,lonmax,d,d2,b,
                                               b2,estacionamientos,bodegas,tipo,operacion,region,comuna,verboso)
                if tipo!='comercial':
                    propiedadesY = from_yapo_select(past, yesterday, preciomin, preciomax, utilmin, utilmax,
                                                                 totalmin, totalmax,
                                                                 latmin, latmax, lonmin, lonmax, d, d2, b,
                                                                 b2, estacionamientos, bodegas, tipo, operacion, region,
                                                                 comuna, "asdasd", "asdasd",
                                                                 "asdasd", "asdasd", "asdasd",latlonyapo, verboso)
                    propiedades=propiedadesP+propiedadesY
                else:
                    propiedades=propiedadesP
                resultado = []

                if verboso:
                    print("[GeneradorReportes] total propiedades encontradas: "+str(len(propiedades)))

                count=0

                for prop in propiedades:
                    try:
                        count=count+1

                        portalinmobiliario= "portalinmobiliario" in prop[14]

                        idProp = prop[15]
                        if portalinmobiliario:
                            if idCliente is not None:
                                ya=yaReportado(idCliente=idCliente,idProp=idProp)
                                if ya[0]:
                                    continue
                                    #fechareporte=ya[1]
                                else:
                                    fechareporte=fechahoy
                            else:
                                fechareporte = fechahoy
                        else:
                             if idCliente is not None:
                                ya=yaReportadoYapo(idCliente=idCliente,idProp=idProp)
                                if ya[0]:
                                    continue
                                    #fechareporte=ya[1]
                                else:
                                    fechareporte=fechahoy
                             else:
                                fechareporte = fechahoy
                        if verboso:
                            print("GeneradorReportes] " + str(count)+"/"+str(len(propiedades)))


                        if metrodistance<999999999:
                            estaciones2=[]
                            for e in estaciones1:
                                subestacion=[]
                                late=e[3]
                                lone=e[4]
                                lat1=prop[10]
                                long1=prop[11]
                                r=6371000
                                c=pi/180
                                distance= 2*r*asin(sqrt(sin(c*(late-lat1)/2)**2 + cos(c*lat1)*cos(c*late)*sin(c*(lone-long1)/2)**2))
                                subestacion.append(e[1])
                                subestacion.append(e[2])
                                subestacion.append(distance)
                                estaciones2.append(subestacion)

                            estaciones2=sorted(estaciones2,key=lambda x:x[2])
                            estacioncercana=estaciones2[0]


                            if metrodistance != None:
                                if estacioncercana[2]>float(metrodistance):
                                    continue


                        subresultado=[]
                        #id
                        print('id2=')
                        print(int(prop[0]))
                        subresultado.append(int(prop[0]))

                        # precio
                        subresultado.append(int(prop[5]))
                        if tipo=="casa":
                            subresultado.append(int(10*(prop[5])/(uf*prop[8]))/10)
                            subresultado.append(int(10*(prop[5])/(uf*prop[9]))/10)
                        else:
                            subresultado.append(int(20*(prop[5])/(uf*(prop[9]+prop[8])))/10)

                        # util
                        subresultado.append(int(prop[8]))
                        # total
                        subresultado.append(int(prop[9]))
                        #Dormitorios
                        subresultado.append(int(prop[6]))
                        #Baños
                        subresultado.append(int(prop[7]))
                        # estacionamiento
                        subresultado.append(int(prop[12]))
                        # Bodega
                        subresultado.append(int(prop[13]))


                        if metrodistance < 999999999:
                            auxestacion="("+str(estacioncercana[0])+") "+str(estacioncercana[1])
                            # metro
                            subresultado.append(auxestacion)
                            # distancia metro
                            subresultado.append(estacioncercana[2])


                        # Aca hacer prediccion
                        # select -> id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,bodegas,link,id
                        # modelo -> dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos
                        if tipo=="comercial":
                            tasacionVenta = clfHV.predict([[prop[8], prop[9], prop[10], prop[11], prop[12]]])
                            tasacionArriendo = clfHA.predict(
                                [[prop[8], prop[9], prop[10], prop[11], prop[12]]])
                        else:
                            tasacionVenta = clfHV.predict([[prop[6], prop[7], prop[8], prop[9], prop[10], prop[11], prop[12]]])
                            tasacionArriendo = clfHA.predict(
                                [[prop[6], prop[7], prop[8], prop[9], prop[10], prop[11], prop[12]]])

                        precioV = tasacionVenta
                        precioA = tasacionArriendo

                        print("el precio tasado de venta inicial es: " + str(precioV))
                        print("el precio tasado de arriendo inicial es: " + str(precioA))

                        print("necesitamos rentabilidades?")
                        print(rentminventa)
                        print(rentminarriendo)
                        if (operacion=="venta" and (rentminventa is not False or rentminarriendo is not False)):

                            if verboso and tipo!= 'comercial':
                                print("[GeneradorReportes] renta promedio para la comuna de: " + str(
                                    comuna) + " para propiedades tipo " + str(tipo) + " de " + str(
                                    int(prop[6])) + " dormitorios, " + str(int(prop[7])) + " baños")



                            if precioV is None or precioV<0.1:
                                if verboso:
                                    print("[GeneradorReportes] Error al predecir precio")
                                continue


                            rentaV=((precioV-prop[5])/prop[5])


                            if rentaV<rentminventa:
                                if verboso:
                                    print("[GeneradorReportes] renta de venta muy baja")
                                continue

                            if precioA is None or precioA<0.01:
                                if verboso:
                                    print("[GeneradorReportes] no existe precio de arriendo")
                                continue

                            rentaA=(precioA*12/prop[5])
                            rentaPP=(precioA*12/precioV)
                            if verboso:
                                print("[GeneradorReportes] rentapp: "+str(rentaPP))
                            if rentaA>0.2:
                                if verboso:
                                    print("[GeneradorReportes] renta de arriendo muy alta")
                                continue

                            if rentaA<0:
                                if verboso:
                                    print("[GeneradorReportes] renta de arriendo muy baja")
                                continue

                            if rentaA<rentminarriendo:
                                if verboso:
                                    print("[GeneradorReportes] renta de arriendo mas baja que minima")
                                continue

                            if rentminventa is not False:
                                # precio venta tasado
                                subresultado.append(precioV)
                                if tipo=="casa":
                                    subresultado.append(int(10*(precioV)/(uf*prop[8]))/10)
                                    subresultado.append(int(10*(precioV)/(uf*prop[9]))/10)
                                else:
                                    subresultado.append(int(20*(precioV)/(uf*(prop[9]+prop[8])))/10)
                                # rentabilidad de venta
                                subresultado.append(float(rentaV))


                            if rentminarriendo is not False:
                                # precio arriendo tasado
                                subresultado.append(precioA)
                                # rentabilidad de arriendo
                                subresultado.append(float(rentaA))


                        else:
                            if rentminarriendo is not False:

                                if precioA is None:
                                    continue

                                # precio arriendo tasado
                                subresultado.append(precioA)
                                rentaA=((precioA-prop[5])/prop[5])
                                if verboso:
                                    print("[GeneradorReportes] arriendo real: "+str(prop[5]))
                                if verboso:
                                    print("[GeneradorReportes] arriendo predicho: "+str(precioA))
                                if verboso:
                                    print("[GeneradorReportes] rentabildiad: "+str(rentaA))
                                if rentaA>1:
                                    continue

                                if rentaA<rentminarriendo:
                                    continue

                                # rentabilidad arriendo
                                subresultado.append(float(rentaA))

                        if not pubPortalExiste.publicacionExiste(prop[14]):
                            if verboso:
                                print("[GeneradorReportes] link no disponible")
                            continue
                        else:
                            # link
                            subresultado.append(prop[14])


                        #agregar mail, telefono y dueño
                        if corredor is not None:
                            if portalinmobiliario:
                                try:
                                    email,telefono,dueno = getDatosDueno(prop[0])
                                    dueno=esDueno(prop[14])
                                    print("es dueño?")
                                    print(dueno)
                                except:
                                    email="NN"
                                    telefono="NN"
                                    dueno="NN"

                            else:
                                email = "NN"
                                telefono = "NN"
                                if (prop[16]==1):
                                    dueno='si'
                                elif (prop[16]==0):
                                    dueno='no'
                                else:
                                    dueno='NN'

                            if (str(dueno) == corredor or (dueno == "NN" and corredor != "a")):
                                if verboso:
                                    print("[GeneradorReportes] La propiedad encontrada " + str(
                                        dueno) + " es gestionada por un dueño")
                                continue


                            subresultado.append(email)
                            subresultado.append(telefono)
                            subresultado.append(dueno)
                            subresultado.append(fechareporte)

                        if rentminventa is not False and operacion=="venta":
                            subresultado.append("confianza venta comming soon")
                        if rentminarriendo is not False:
                            subresultado.append("confianza arriendo comming soon")

                        if verboso:
                            print("[GeneradorReportes] depto encontrado para "+nombreCliente)

                        # try:
                        #     if rentaV>0.25:
                        #
                        #         sendMailOportunidad.sendMail(columnNames,subresultado)
                        # except:
                        #     pass
                        resultado.append(subresultado)
                        #print("sub appended")

                        if idCliente is not None:
                            if portalinmobiliario:
                                guardarRegistro(idCliente, idProp, fechareporte)
                            else:
                                guardarRegistroYapo(idCliente,idProp,fechareporte)
                    except Exception as e:
                        print(e)
                        continue
                if len(resultado)>0:
                    if verboso:
                        print("[GeneradorReportes] Generando Reporte para el cliente "+nombreCliente)


                    if ((prioridad=="arriendo") and rentminarriendo is not None):
                        index = columnNames.index("Rent. Arriendo")
                        resultado=sorted(resultado, key=lambda x:x[index],reverse=True)
                    elif ((prioridad=="venta") and (rentminventa is not None)):
                        index = columnNames.index("Rent. Venta")
                        resultado=sorted(resultado, key=lambda x:x[index],reverse=True)
                    else:
                        resultado=sorted(resultado, key=lambda x:x[1])


                    if topx is not None:
                        resultado=resultado[:topx]
                    #if (operacion=="venta"):
                     #   columnNames=["Precio","Útil","Tot","Estacionamiento","Metro","Dist-est.","P.P","Rent.V","Arriendo","Rent.A","Link"]
                    #else:
                     #   columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","Arriendo","Rent.A","Link"]

                    if (nombreCliente is None):
                        nombreCliente = "otros"

                    nombreCliente=nombreCliente.replace('á','a')
                    nombreCliente=nombreCliente.replace('é','e')
                    nombreCliente=nombreCliente.replace('í','i')
                    nombreCliente=nombreCliente.replace('ó','o')
                    nombreCliente=nombreCliente.replace('ú','u')
                    nombreCliente=nombreCliente.replace('ü','u')
                    nombreCliente=nombreCliente.replace('ñ','n')

                    nombreComuna=str(comuna).replace('á','a')
                    nombreComuna=nombreComuna.replace('é','e')
                    nombreComuna=nombreComuna.replace('í','i')
                    nombreComuna=nombreComuna.replace('ó','o')
                    nombreComuna=nombreComuna.replace('ú','u')
                    nombreComuna=nombreComuna.replace('ü','u')
                    nombreComuna=nombreComuna.replace('ñ','n')

                    if separado:
                        nombreArchivo = "reporte " + nombreCliente + " " + str(tipo) + " " + nombreComuna + " " + str(
                            d) + " " + str(b) + " " + str(fechahoy) + '.xlsx'
                    else:
                        nombreArchivo = "reporte " + nombreCliente + " " + str(tipo) + " " + str(operacion) + " " + nombreComuna + " "+ str(fechahoy) + '.xlsx'
                    if (nombrecarpetadb is None):
                        patharchivo = os.path.join(os.path.expanduser('~'), 'temp' ,nombreArchivo)

                    else:
                        crearCarpetaSiNoExiste(nombrecarpetadb,fechahoy,nombreCliente)
                        print("carpeta encontrada,  o creada")
                        patharchivo = os.path.join(os.path.expanduser('~'), 'Dropbox', 'Reportes', str(nombrecarpetadb), str(nombreCliente),str(fechahoy),nombreArchivo)
                        print(patharchivo)
                        #writeCsv(nombreArchivo, resultado, columnNames, operacion)


                    writeXlsx(patharchivo,resultado,columnNames,operacion)

                    listaAdjuntos.append(patharchivo)
                    print(listaAdjuntos)
                    if verboso:
                        print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)
                else:
                    if verboso:
                        print("[GeneradorReportes] No se han encontrado propiedades para el cliente "+nombreCliente)
                        continue
                if separado is False:
                    break

            if separado is False:
                break

    #Arreglar Mandada de mails
    if len(listaAdjuntos)>0:
        print('proceder a mandar correo')
        sendmail.sendMailMultipleText(mail, nombreCliente, listaAdjuntos,textmail)
        return True
    else:
        return 'No Se han encontrado propiedades para el reporte solicitado'

    #borrar archivos si no habia carpeta de DB
    if nombrecarpetadb is None:
        for archivo in listaAdjuntos:
            os.remove(archivo)


if __name__ == '__main__':
    #main()
    # generarReporte(preciomin=70000000, preciomax=140000000,utilmin=0,utilmax=99,totalmin=0,totalmax=99,latmin=-9999,
    #                latmax=9999,lonmin=-9999,lonmax=9999,dormitoriosmin=1,dormitoriosmax=2,banosmin=1,banosmax=2,
    #                confmin=8,rentmin=0.00,estacionamientos=1,metrodistance=9999,tipo='departamento',operacion='venta',
    #                region='metropolitana',comuna1='vitacura',comuna2='asdasdasd',comuna3='asdasd',comuna4='asdasdasd',
    #                comuna5='asdasd',comuna6='asdasdasd',prioridad='arriendo',flagMail=1,mail='joaquin.gonzalez@alumnos.usm.cl',
    #                nombreCliente='PruebaSergei',verboso=True)

    generarReporteSeparado(preciomin=20000000, preciomax=60000000,utilmin=0,utilmax=99,totalmin=0,totalmax=99,latmin=-9999,
                   latmax=9999,lonmin=-9999,lonmax=9999,dormitoriosmin=1,dormitoriosmax=1,banosmin=1,banosmax=2,
                   confmin=8,rentminventa=0.15,rentminarriendo=0.05,estacionamientos=0,metrodistance=9999,tipo='departamento',operacion='venta',
                   region='metropolitana',comuna1='la-cisterna',comuna2='asdasdasd',comuna3='asdasd',comuna4='asdasdasd',
                   comuna5='asdasd',comuna6='asdasdasd',prioridad='venta',flagMail=2,mail='sergei.schkolnik@gmail.com',
                   nombreCliente='la-cisterna-1-1',verboso=True, separado=True)
