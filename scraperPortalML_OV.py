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

headers = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1',
    'viewport-width': '1920',
    'rtt': '50',
    'downlink': '10',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.portalinmobiliario.com/venta/departamento/valparaiso',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=451a14f3-4e31-4e39-8437-0c61431860bf-n; _csrf=nre_frMxdtmQDlFHoqwBFzJ_; c_home=0.20.0%7C5.3.3; pin_d2id=; pin_exp=new; _d2id=451a14f3-4e31-4e39-8437-0c61431860bf; _pi_ga=GA1.2.1908173662.1572265564; _pi_ga_gid=GA1.2.875034433.1572265564; _pi_ci=1908173662.1572265564; _pi_dc=1; _hjid=26bec885-e436-45d1-9d66-9acc89939111; _hjIncludedInSample=1; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiJWYWxwYXJh7XNvIiwic2VsZWN0ZWQiOiJUVXhEVUZaQlRFODRNRFZqIn0sImZpbHRlci1uZXciOnsiY2hlY2tlZCI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZX19; _mlt=2053cd3b-2b2f-4153-b641-c2fa3d0cd68a',
}


dormitorios = ["sin-dormitorios",
                "1-dormitorio",
                "2-dormitorios",
                "3-dormitorios",
                "mas-de-4-dormitorios"]
banos = ["_Banos_1",
          "_Banos_2",
          "_Banos_3",
          "_Banos_4",
          "_Banos_5-o-mas"]


tipos=["departamento","casa","comercial","parcela","oficina","industrial","agricola","terreno-en-construccion","bodega","estacionamiento"]
operaciones = ["venta","arriendo"]
pages = range(1,2050,50)

uf = uf.getUf()


def obtenerBodegas(texto):
    bodegas = 0

    texto = texto.lower()

    visitas = ['bodega de visita', 'bodegas de visita', 'bodega visita', 'bodegas visita', 'bodega para visita',
               'bodegas para visita']
    for vis in visitas:
        if (vis in texto):
            texto = texto.replace(vis, '')

    if 'bodegas: 0' in texto:
        bodegas = 0
    elif 'bodegas: 1' in texto:
        bodegas = 1
    elif 'bodegas: 2' in texto:
        bodegas = 2
    elif 'bodegas: 3' in texto:
        bodegas = 3
    elif ('in bodega' in texto):
        bodegas = 0
    elif ('bodega: n' in texto):
        bodegas = 0
    elif ('bodega' in texto):
        if ('incluye bodega' in texto):
            if ('no incluye bodega' in texto):
                bodegas = 0
            elif ('ni incluye bodega' in texto):
                bodegas = 0
            elif ('tampoco incluye bodega' in texto):
                bodegas = 0
            else:
                bodegas = 1

        elif ('tiene bodega' in texto):
            if ('no tiene bodega' in texto):
                bodegas = 0
            elif ('ni tiene bodega' in texto):
                bodegas = 0
            else:
                bodegas = 1

        elif ('con bodega' in texto):
            if ('cuenta con bodega' in texto):
                if ('no cuenta con bodega' in texto):
                    bodegas = 0
                elif ('ni cuenta con bodega' in texto):
                    bodegas = 0
                elif ('tampoco cuenta con bodega' in texto):
                    bodegas = 0
                else:
                    bodegas = 1
            elif ('viene con bodega' in texto):
                if ('no viene con bodega' in texto):
                    bodegas = 0
                elif ('ni viene con bodega' in texto):
                    bodegas = 0
                else:
                    bodegas = 1
            else:
                bodegas = 1
        elif (('ni bodega' in texto) or ('no bodega' in texto)):
            bodegas = 0

        elif (('sin bodega' in texto)):
            bodegas = 0

        elif ('tiene bodega' in texto):
            if ('no tiene bodega' in texto):
                bodegas = 0
            elif ('ni tiene bodega' in texto):
                bodegas = 0
            else:
                bodegas = 1
        elif ('posee bodega' in texto):
            if ('no posee bodega' in texto):
                bodegas = 0
            elif ('ni posee bodega' in texto):
                bodegas = 0
            else:
                bodegas = 1

        else:
            bodegas = 1
    return bodegas


def obtenerEstacionamientos(texto):
    estacionamientos = 0

    texto = texto.lower()

    visitas = ['estacionamiento de visita', 'estacionamientos de visita', 'estacionamiento visita',
               'estacionamientos visita', 'estacionamiento para visita', 'estacionamientos para visita']
    for vis in visitas:
        if (vis in texto):
            texto = texto.replace(vis, '')

    if 'estacionamientos: 0' in texto:
        estacionamientos = 0
    elif 'estacionamientos: 1' in texto:
        estacionamientos = 1
    elif 'estacionamientos: 2' in texto:
        estacionamientos = 2
    elif 'estacionamientos: 3' in texto:
        estacionamientos = 3
    elif ('in estacionamiento' in texto):
        estacionamientos = 0
    elif ('estacionamiento: n' in texto):
        estacionamientos = 0
    elif ('estacionamiento' in texto):
        if ('incluye estacionamiento' in texto):
            if ('no incluye estacionamiento' in texto):
                estacionamientos = 0
            elif ('ni incluye estacionamiento' in texto):
                estacionamientos = 0
            elif ('tampoco incluye estacionamiento' in texto):
                estacionamientos = 0
            else:
                estacionamientos = 1

        elif ('tiene estacionamiento' in texto):
            if ('no tiene estacionamiento' in texto):
                estacionamientos = 0
            elif ('ni tiene estacionamiento' in texto):
                estacionamientos = 0
            else:
                estacionamientos = 1

        elif ('con estacionamiento' in texto):
            if ('cuenta con estacionamiento' in texto):
                if ('no cuenta con estacionamiento' in texto):
                    estacionamientos = 0
                elif ('ni cuenta con estacionamiento' in texto):
                    estacionamientos = 0
                elif ('tampoco cuenta con estacionamiento' in texto):
                    estacionamientos = 0
                else:
                    estacionamientos = 1
            elif ('viene con estacionamiento' in texto):
                if ('no viene con estacionamiento' in texto):
                    estacionamientos = 0
                elif ('ni viene con estacionamiento' in texto):
                    estacionamientos = 0
                else:
                    estacionamientos = 1
            else:
                estacionamientos = 1
        elif (('ni estacionamiento' in texto) or ('no estacionamiento' in texto)):
            estacionamientos = 0

        elif (('sin estacionamiento' in texto)):
            estacionamientos = 0

        elif ('tiene estacionamiento' in texto):
            if ('no tiene estacionamiento' in texto):
                estacionamientos = 0
            elif ('ni tiene estacionamiento' in texto):
                estacionamientos = 0
            else:
                estacionamientos = 1
        elif ('posee estacionamiento' in texto):
            if ('no posee estacionamiento' in texto):
                estacionamientos = 0
            elif ('ni posee estacionamiento' in texto):
                estacionamientos = 0
            else:
                estacionamientos = 1

        else:
            estacionamientos = 1

    return estacionamientos

def error(link,texto):

    f = open("errores " + str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().month) + '-' + str(
        datetime.datetime.now().year) + ".txt", "a+")
    print("[PIOV][ERROR] " + str(datetime.datetime.now()) + ',' + link + "," + str(texto))
    f.write("[PIOV]"+str(datetime.datetime.now()) + ',' + link + "," + str(texto) + "\n\n")
    f.close()

def actualizar_checker(operacion,tipo,region,pagina):
    d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE checker SET lastscrap='"+str(d)+"',operacion='" + operacion + "',tipo='"+ tipo +"',region='"+ region +"',pagina="+str(pagina)+" WHERE nombrescraper='spivm'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    mariadb_connection.commit()
    mariadb_connection.close()

def insertarDueno(dueno):
    #Inserta un dueño en una base de datos

    sql = """INSERT INTO duenos(idProp,mail,telefono,esDueno)
             VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE telefono=%s, esDueno=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (dueno))

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

def scrap(linkList,region,operacion,tipo,hoja):

    for i,link in enumerate(linkList):

        print("[PIOV]" + str(i + 1 + hoja) + " - " + str(region) + " - " + str(operacion) + " - " +
            str(tipo))

        time.sleep(random.randint(1,3))
        try:
            request = requests.get(link, headers=headers)
        except:
            time.sleep(random.randint(60,90))
            request = requests.get(link, headers=headers)

        try:
            tree = html.fromstring(request.content)
        except:
            #   print("Fallo.")
            error(link,"Error al tratar de crear tree.")
            continue

        priceSymbolPath = '//*[@id="productInfo"]/fieldset/span/span[1]'

        pricePath = '//*[@id="productInfo"]/fieldset/span/span[2]'
        namePath = '//*[@id="short-desc"]/div/header/h1'
        addressPath = '//*[@id="root-app"]/div/div/div[1]/div[3]/section/div[1]/div/h2'

        priceSymbol = tree.xpath(priceSymbolPath)
        if len(priceSymbol) == 0:
            error(link,"Error al sacar el simbolo de precio")
            continue

        priceSymbol = priceSymbol[0].text
        price = tree.xpath(pricePath)
        if len(price) == 0:
            error(link,"Error al sacar precio")
            continue
        price = int(price[0].text.replace(',','').replace(' ','').replace('.',''))

        if priceSymbol == 'UF':
            price = price*uf

        name = tree.xpath(namePath)
        if len(name) == 0:
            error(link,"Error al sacar nombre")
            continue

        name = name[0].text.replace('\n','').replace('\t','')

        address =  tree.xpath(addressPath)
        if len(address) == 0:
            error(link,"Error al sacar nombre")
            address = '-'
        else:
            address = address[0].text

        #fecha
        datePosition = request.text.find('<p class="title">Fecha de Publicación</p>')
        if datePosition == -1:
            error(link,"Error al sacar fecha")
            date = "00-00-0000"
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
        minMetersFound = maxMetersFound = estacionamientosFound = bodegasFound = False

        try:
            for j, element in enumerate(htmlArray):
                if j == len(htmlArray)-1:
                    #last element, we have to split again.
                    element = element.split('</ul>')[0]
                if "Superficie total" in element and not maxMetersFound:
                    maxMeters = int(float(element.split('span')[1][1:-5]))
                    maxMetersFound = True
                elif "Superficie útil" in element and not minMetersFound:
                    minMeters = element.split('span')[1][1:-5]
                    minMetersFound = True
                elif "Estacionamientos" in element and not estacionamientosFound:
                    estacionamientos = int(
                        float(element.split('span')[1].replace('<', '').replace('>', '').replace('/', '')))
                    estacionamientosFound = True
                elif "Bodegas" in element and not bodegasFound:
                    bodegas = int(float(element.split('span')[1].replace('<', '').replace('>', '').replace('/', '')))
                    bodegasFound = True
        except:
            error(link, "Error en superficies, estacionamientos o bodegas.")
            continue
        if maxMeters != 0 and minMeters == 0:
            minMeters = maxMeters
        if minMeters != 0 and maxMeters == 0:
            maxMeters = minMeters

        #baños y dormitorios
        try:
            item1xpath = '//*[@id="productInfo"]/div[1]/dl[1]/dd'
            item2xpath = '//*[@id="productInfo"]/div[1]/dl[2]/dd'
            item3xpath = '//*[@id="productInfo"]/div[1]/dl[3]/dd'
            itemUniquexpath = '//*[@id="productInfo"]/div[1]/dl/dd'

            item1 = tree.xpath(item1xpath)
            item2 = tree.xpath(item2xpath)
            item3 = tree.xpath(item3xpath)
            itemU = tree.xpath(itemUniquexpath)

            item1 = item1[0].text if len(item1) > 0 else ''
            item2 = item2[0].text if len(item2) > 0 else ''
            item3 = item3[0].text if len(item3) > 0 else ''
            itemU = itemU[0].text if len(itemU) > 0 else ''

            if "dormitorio" in item1:
                dorms = int(item1.split(' ')[0])
            elif "dormitorio" in item2:
                dorms = int(item2.split(' ')[0])
            elif "dormitorio" in item3:
                dorms = int(item3.split(' ')[0])
            elif "dormitorio" in itemU:
                dorms = int(itemU.split(' ')[0])
            elif "priva" in item1:
                dorms = int(item1.split(' ')[0])
            elif "priva" in item2:
                dorms = int(item2.split(' ')[0])
            elif "priva" in item3:
                dorms = int(item3.split(' ')[0])
            elif "priva" in itemU:
                dorms = int(itemU.split(' ')[0])
            else:
                dorms = 0

            if "baño" in item1:
                baths = int(item1.split(' ')[0])
            elif "baño" in item2:
                baths = int(item2.split(' ')[0])
            elif "baño" in item3:
                baths = int(item3.split(' ')[0])
            elif "baño" in itemU:
                baths = int(itemU.split(' ')[0])
            else:
                baths = 0
        except:
            error(link,"Error en baños o dormitorios")


        #lat, lon
        mapPosition = request.text.find("center=")
        if mapPosition == -1:
            error(link,"Error in finding map")
            lat = 0
            lon = 0
        else:
            amperPosition = request.text[mapPosition:].find('&')
            mapTexts = request.text[mapPosition:mapPosition+amperPosition].replace("center=",'').split('%2C')
            lat = float(mapTexts[0])
            lon = float(mapTexts[1])

        fechascrap = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

        propiedad = []

        try:
            code=int(link.split('/')[6].split('-')[0])
        except Exception as err:
            try:
                code = int(link.split('/')[3].split('-')[1])
            except Exception as err2:
                error(link, "Error al obtener el codigo de portalinmobiliario:" + str(err2))
                continue


        #text mining para bodegas
        if bodegas == 0:
            descripcion_xpath  = '//*[@id="description-includes"]/div/p'
            descripcion_result = tree.xpath(descripcion_xpath)
            if len(descripcion_result)>0:
                bodegas = obtenerBodegas(descripcion_result[0].text)

        # text mining para estacionamientos
        if estacionamientos == 0:
            descripcion_xpath = '//*[@id="description-includes"]/div/p'
            descripcion_result = tree.xpath(descripcion_xpath)
            if len(descripcion_result) > 0:
                estacionamientos = obtenerEstacionamientos(descripcion_result[0].text)

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
            error(link,"Error al escribir en BD:" + str(err))
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
            error(link, "Error al sacar telefono propietario.")
            phone = ""
        dueno.append(phone)
        dueno.append(esPropietario)
        dueno.append(phone)
        dueno.append(esPropietario)

        try:
            insertarDueno(dueno)
        except Exception as err:
            error(link, "Error al insertar dueno:" + str(err))
            pass
        # fin sector dueño




def main():

    for tipo in tipos:
        for operacion in operaciones:
            if tipo=='casa' or tipo=='departamento':
                for bano in banos:
                    for dormitorio in dormitorios:
                        for page in pages:
                            time.sleep(random.randint(5,7))

                            if(page==1):
                                page=0

                            link = "https://www.portalinmobiliario.com/"+operacion+"/"+tipo+"/propiedades-usadas/"+\
                                   dormitorio+"/valparaiso/"+bano+"_desde_"+str(page)
                            print(link)
                            request = requests.get(link, headers =headers)

                            try:
                                tree = html.fromstring(request.content)
                            except:
                                break

                            resultBoxXpath = '//*[@id="results-section"]'
                            results = tree.xpath(resultBoxXpath)
                            if len(results) == 0:
                                #no results
                                break

                            #revisar no pasarse del nr de resultados
                            nrResultsPath = '//*[@id="inner-main"]/aside/div[2]'
                            try:
                                results2 = int(tree.xpath(nrResultsPath)[0].text.split(" ")[1].replace(".",""))
                                if page > results2:
                                    break
                            except:
                                break

                            resultLinkList = []

                            htmlArray = request.text.split(" ")
                            for element in htmlArray:
                                if "item-url=" in element:
                                    result_link = element.replace('"', '').replace("item-url=", "")
                                    result_link = result_link.split('#')[0]
                                    resultLinkList.append(result_link)

                            scrap(linkList=resultLinkList,region="valparaiso",operacion=operacion, tipo=tipo,
                                  hoja=page)

            else:
                for page in pages:
                    time.sleep(random.randint(1, 3))

                    link = "https://www.portalinmobiliario.com/"+operacion+"/"+tipo+"/propiedades-usadas/valparaiso/_desde_"+str(page)
                    print(link)
                    request = requests.get(link, headers=headers)

                    try:
                        tree = html.fromstring(request.content)
                    except:
                        break

                    resultBoxXpath = '//*[@id="results-section"]'
                    results = tree.xpath(resultBoxXpath)
                    if len(results) == 0:
                        # no results
                        break

                    #revisar no pasarse del nr de resultados
                    nrResultsPath = '//*[@id="inner-main"]/aside/div[2]'
                    try:
                        results2 = int(tree.xpath(nrResultsPath)[0].text.split(" ")[1].replace(".",""))
                        if page > results2:
                            break
                    except:
                        break

                    resultLinkList = []

                    htmlArray = request.text.split(" ")
                    for element in htmlArray:
                        if "item-url=" in element:
                            result_link = element.replace('"', '').replace("item-url=", "")
                            resultLinkList.append(result_link)

                    scrap(linkList=resultLinkList, region="metropolitana", operacion=operacion, tipo=tipo, hoja=page)

if __name__ == "__main__":
    while(True):
        main()




