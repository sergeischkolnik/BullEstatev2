import requests
from lxml import html
import math
import agentCreator
import time
import random
from bs4 import BeautifulSoup
import datetime
import pymysql as mysql
import uf

headers1 = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; PI=d50qlpmdqz1qdv4lynbllh0w; __RequestVerificationToken=NK9YOkOtc3k6bUsfzF0OyZa_kYCBJlPtdTSyYK97lihubPSwAGhZp8pigJ1j5S6LOPG3PlvaiaCMpSoomr7Ez00OFHw1; uniqueID=4df06d9b-bd2e-4565-bff5-9d30c15ea7b2; _ga=GA1.1.434386957.1551705638; _hjid=f5243996-1bed-4c3a-9d9b-0468976dd33e; Buscador=Region=356&IDBusquedaUnidadGeopolitica=356&TipoPropiedad=Departamento; AWSELB=7517F7ED0C3C5C3E0C8743D6A3E725F2C6421325348258AB2B2B6C24C55B97E7B421F62FEDE1E3B33663FE99C845602640543858273DAF905910FD5E38A1B2D3F9329B42B1; _mlt=d8ec613f-94d1-479b-9224-07a09b8ecc69; pin_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; _pi_ga=GA1.2.901507403.1570560325; _pi_ci=901507403.1570560325; _d2id=10753c94-136c-426d-b536-52f4bdc9ad06; _csrf=wiPGYePC-rZQJpMMJMEqYZv_; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiJwcm92aWRlbmNpYSIsInNlbGVjdGVkIjoiIn0sImZpbHRlci1uZXciOnsiY2hlY2tlZCI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZX19; JSESSIONID=4EE983A7EB482E20624672E4E17AF4E8; pmsctx=******IMLC507223027%7C%7CIMLC507775718%7CIMLC508093497%7C%7C**; navigation_items=MLC507223027%7C14102019125752-MLC507775718%7C14102019125042-MLC508093497%7C08102019190408-MLC507769027%7C08102019184813-MLC507748684%7C08102019184550; c_home=0.0.6-redirect-circular-ref%7C5.2.0; pin_exp=new; _pi_ga_gid=GA1.2.1582383825.1571164864',
}

headers2 = {
    'authority': 'www.google.com',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1',
    'viewport-width': '1920',
    'rtt': '100',
    'downlink': '4.35',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'nested-navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'cross-site',
    'referer': 'https://www.portalinmobiliario.com/MLC-509232849-sn-martin575-vistamar-2d-lado-playacasino-cestacionamient-_JM',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': 'NID=189=d1T2vt5csSsrUd5KBdpdFAFv6Etc2ggAwQC5hSdVVPg_x0VGNrkl8Qxw6Pgyleov_j7CXq0qncsjCMtjOwniOpJ__p5_OmGwev7LBVyMc4o9Vw8Lsw2et0j-gFbv5l8MyIA-F9Em4w_2wFMFJVhtIT4Hewe6bybpVureG_4keJA',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://www.google.com/recaptcha/api2/webworker.js?hl=es-419&v=xw1jR43fRSpRG88iDviKn3qM',
    'Origin': 'https://www.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'text/plain',
    'Upgrade-Insecure-Requests': '1',
}

headers3 = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1',
    'viewport-width': '1920',
    'rtt': '50',
    'downlink': '10',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=6f449319-f0db-4852-b6e6-4473d31fff5d-n; _mlt=6a76c9f9-c776-47f0-bf16-8e3bf8ea1091; uniqueID=15965c7c-9edb-43df-9c85-f4dac69268ea; _pi_ga=GA1.2.2067791864.1571058095; _pi_ci=2067791864.1571058095; _d2id=6f449319-f0db-4852-b6e6-4473d31fff5d; _hjid=eb71f50e-8d3c-489e-9792-11a7f5617768; _csrf=WaWxAUx6HMKTob31r4cf-3mz; c_home=0.0.6-redirect-circular-ref%7C5.2.0; pin_d2id=6f449319-f0db-4852-b6e6-4473d31fff5d; pin_exp=new; _pi_ga_gid=GA1.2.996463285.1571231021; JSESSIONID=FFF44D40DDF915344000286569A64337; pmsctx=******IMLC509232849%7C%7CIMLC507223027%7C%7C%7C**; navigation_items=MLC509232849%7C16102019130355-MLC507223027%7C14102019130557; _pi_dc=1',
}


headerList = [headers1,headers2,headers3]


dormitorios = range(1,10)
banos = range(1,10)
comunas = ["santiago","providencia","las-condes","cerrillos","colina","cerro-navia","conchali","el-bosque","estacion-central","huechuraba","independencia",
           "la-cisterna","la-florida","la-granja","la-pintana","la-reina","lampa","lo-barnechea","lo-espejo",
           "lo-prado","macul","paine","penalolen","puente-alto","pedro-aguirre-cerda","penaflor",
           "pudahuel","quilicura","quinta-normal","recoleta","renca","san-bernardo","san-miguel","san-ramon",
           "san-joaquin","san-pedro","talagante","vitacura","nunoa"]
pages = range(0,2050,50)

uf = uf.getUf()

def error(link,texto):

    f = open("errores " + str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
        datetime.datetime.now().year) + ".txt", "a+")
    print(str(datetime.datetime.now()) + ',' + link + "," + str(texto))
    f.write("[ERROR] " + str(datetime.datetime.now()) + ',' + link + "," + str(texto) + "\n\n")
    f.close()

def actualizar_checker(operacion,tipo,region,pagina):
    d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE checker SET lastscrap='"+str(d)+"',operacion='" + operacion + "',tipo='"+ tipo +"',region='"+ region +"',pagina="+str(pagina)+" WHERE nombrescraper='spivm'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    mariadb_connection.commit()
    mariadb_connection.close()

def insertarPropiedad(propiedad):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO portalinmobiliario(id2,nombre,fechapublicacion,fechascrap,region,direccion,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nombre=%s,fechapublicacion=%s,fechascrap=%s,region=%s,direccion=%s,operacion=%s,tipo=%s,precio=%s,dormitorios=%s,banos=%s,metrosmin=%s,metrosmax=%s,estacionamientos=%s,bodegas=%s,lat=%s,lon=%s,link=%s"""
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))
    mariadb_connection.commit()
    mariadb_connection.close()

def insertarDueno(dueno):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO duenos(idProp,mail,telefono,esDueno)
             VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE telefono=%s, esDueno=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (dueno))

    mariadb_connection.commit()
    mariadb_connection.close()

def scrap(linkList,region,operacion,comuna,tipo,dorms,baths):
    fechascrap = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
        datetime.datetime.now().day)

    headerIndex = 0



    for i,link in enumerate(linkList):

        print(str(i)+"/"+str(len(linkList)) + " - " + str(region) + " - " + str(comuna) + " - "+str(operacion) + " - " +
              str(tipo) + " - " + str(dorms) + " - " + str(baths))

        time.sleep(random.randint(1,3))
        request = requests.get(link, headers=headerList[headerIndex])
        headerIndex += 1
        headerIndex = headerIndex % len(headerList)
        try:
            tree = html.fromstring(request.content)
        except:
            error(link,"Error al crear tree.")
            continue

        priceSymbolPath = '//*[@id="productInfo"]/fieldset/span/span[1]'

        pricePath = '//*[@id="productInfo"]/fieldset/span/span[2]'
        namePath = '//*[@id="short-desc"]/div/header/h1'

        addressPath = '//*[@id="root-app"]/div/div/div[1]/div[3]/section/div[1]/div/h2'

        priceSymbol = tree.xpath(priceSymbolPath)
        if len(priceSymbol) == 0:
            error(link, "Error al sacar el simbolo de precio")
        priceSymbol = priceSymbol[0].text
        price = tree.xpath(pricePath)
        if len(price) == 0:
            error(link, "Error al sacar el precio")
            continue
        price = int(price[0].text.replace(',','').replace(' ','').replace('.',''))

        if priceSymbol == 'UF':
            price = price*uf

        name = tree.xpath(namePath)
        if len(name) == 0:
            error(link, "Error al sacar el nombre")
            continue

        name = name[0].text.replace('\n','').replace('\t','')

        address =  tree.xpath(addressPath)
        if len(address) == 0:
            error(link, "Error al sacar el direccion")
            address = '-'
        else:
            address = address[0].text

        #fecha
        datePosition = request.text.find('<p class="title">Fecha de Publicación</p>')
        if datePosition == -1:
            error(link, "Error al sacar fecha")
            date = "1900-01-01"
        else:
            date = request.text[datePosition+60:datePosition+70]
            dateSplit = date.split('-')
            date = dateSplit[2] + '-' + dateSplit[1] + '-' + dateSplit[0]

        #metraje, estacionamientos, bodegas
        htmlArray = request.text.split('<li class="specs-item">')
        maxMeters = 0
        minMeters = 0
        estacionamientos = 0
        bodegas = 0
        try:
            for element in htmlArray:
                if "Superficie total" in element:
                    maxMeters = int(float(element.split('span')[1][1:-5]))
                elif "Superficie útil" in element:
                    minMeters = int(float(element.split('span')[1][1:-5]))
                elif "Estacionamientos" in element:
                    estacionamientos = int(float(element.split('span')[1].replace('<','').replace('>','').replace('/','')))
                elif "Bodegas" in element:
                    bodegas = int(float(element.split('span')[1].replace('<','').replace('>','').replace('/','')))
        except Exception as err:
            error(link, "Error en bloque de info")
            continue

        if maxMeters != 0 and minMeters == 0:
            minMeters = maxMeters
        if minMeters != 0 and maxMeters == 0:
            maxMeters = minMeters


        #lat, lon
        mapPosition = request.text.find("center=")
        if mapPosition == -1:
            error(link, "Error al buscar imagen de mapa")
            lat = 0
            lon = 0
        else:
            amperPosition = request.text[mapPosition:].find('&')
            mapTexts = request.text[mapPosition:mapPosition+amperPosition].replace("center=",'').split('%2C')
            lat = float(mapTexts[0])
            lon = float(mapTexts[1])



        propiedad = []
        try:
            code=int(link.split('/')[6].split('-')[0])

        except Exception as err:
            error(link, "Error al sacar codigo")
            continue

        propiedad.append(code)
        propiedad.append(name)
        propiedad.append(date)
        propiedad.append(fechascrap)
        propiedad.append(region)
        propiedad.append(address)
        propiedad.append(operacion)
        propiedad.append(tipo)
        propiedad.append(price)
        propiedad.append(dorms)
        propiedad.append(baths)
        propiedad.append(minMeters)
        propiedad.append(maxMeters)
        propiedad.append(estacionamientos)
        propiedad.append(bodegas)
        propiedad.append(lat)
        propiedad.append(lon)
        propiedad.append(link)
        propiedad.append(name)
        propiedad.append(date)
        propiedad.append(fechascrap)
        propiedad.append(region)
        propiedad.append(address)
        propiedad.append(operacion)
        propiedad.append(tipo)
        propiedad.append(price)
        propiedad.append(dorms)
        propiedad.append(baths)
        propiedad.append(minMeters)
        propiedad.append(maxMeters)
        propiedad.append(estacionamientos)
        propiedad.append(bodegas)
        propiedad.append(lat)
        propiedad.append(lon)
        propiedad.append(link)


        try:
            insertarPropiedad(propiedad)
        except Exception as err:
            error(link, "Error en insercion de propiedad:"+str(err))
            continue

        # verificar si es dueño y crear objeto dueño
        agency_path = '//*[@id="real_estate_agency"]'
        agency = tree.xpath(agency_path)
        esPropietario = "no"
        if len(agency) == 0:
            # no hay agency; es dueño.
            esPropietario = "si"
        dueno = []
        dueno.append(str(code))
        dueno.append(None)
        phone_path = '//*[@id="root-app"]/div/div[1]/div[2]/section[1]/p[3]/span/span[1]/text()'
        phoneElem = tree.xpath(phone_path)
        try:
            if len(phoneElem) > 0:
                phone = str(phoneElem[0])
            else:
                phone_path = '//*[@id="root-app"]/div/div[1]/div[2]/section[1]/p[5]/span/span/text()'
                phoneElem = tree.xpath(phone_path)
                phone = str(phoneElem[0])
        except:
            error(link,"Error al sacar telefono propietario.")
            phone = ""
        dueno.append(phone)
        dueno.append(esPropietario)
        dueno.append(phone)
        dueno.append(esPropietario)

        try:
            insertarDueno(dueno)
        except Exception as err:
            error(link, "Error al insertar dueno:"+str(err))
            pass
        # fin sector dueño


def main():
    headerIndex = 0
    for comuna in comunas:
        for dormitorio in dormitorios:
            for bano in banos:
                if math.fabs(bano-dormitorio) > 4:
                    continue
                for page in pages:
                    time.sleep(random.randint(1,4))
                    dorm_text = "sin-dormitorios" if dormitorio==0 else str(dormitorio)+"-dormitorio"
                    link = "https://www.portalinmobiliario.com/venta/departamento/propiedades-usadas/"+dorm_text+"/"+comuna+"-metropolitana/_Desde_"+str(page)+"_Banos_"+str(bano)
                    print(link)
                    request = requests.get(link, headers = headerList[headerIndex])

                    headerIndex += 1
                    headerIndex = headerIndex % len(headerList)

                    try:
                        tree = html.fromstring(request.content)
                    except:
                     #   print("Fallo.")
                        break

                    resultBoxXpath = '//*[@id="results-section"]'
                    results = tree.xpath(resultBoxXpath)
                    if len(results) == 0:
                        #no results
                        break

                    resultLinkList = []

                    htmlArray = request.text.split(" ")
                    for element in htmlArray:
                        if "item-url=" in element:
                            result_link = element.replace('"', '').replace("item-url=", "")
                            result_link = result_link.split('#')[0]
                            resultLinkList.append(result_link)

                    scrap(linkList=resultLinkList,region="metropolitana",operacion="venta",comuna=comuna,
                          tipo="departamento",dorms=dormitorio,baths=bano)

main()



