import math
from lxml import html
import requests
import datetime
from threading import Thread
import pymysql as mysql
from itertools import cycle
import agentCreator
import time
import random
from requests_html import HTMLSession
session = HTMLSession()

print("[SPIVDM] " + str(datetime.datetime.now()))

# def rotateToFirst(l, element):
#     if element in l:
#         return l[l.index(element):] + l[:l.index(element)]
#     else:
#         return l

def actualizar_checker(operacion,tipo,region,pagina):
    d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE checker SET lastscrap='"+str(d)+"',operacion='" + operacion + "',tipo='"+ tipo +"',region='"+ region +"',pagina="+str(pagina)+" WHERE nombrescraper='spivdm'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    mariadb_connection.commit()
    mariadb_connection.close()

def get_proxiestextweb():
    url="https://proxyscrape.com/proxies/HTTP_Working_Proxies.txt"
    proxies=set()
    response=requests.get(url)
    ip=response.text.split('\r\n')
    for proxy in ip:
            proxies.add(proxy)
    return proxies

def getLast(operacion,tipo,region,proxi):
    #Obtiene el número de la última página con publicaciones

    #armar link a consultar dada una operacion, tipo, region
    link='https://www.portalinmobiliario.com/'+str(operacion)+'/'+str(tipo)+'/'+str(region)+'?ca=2&ts=1&mn=2&or=p-asc&pg=1&sf=0&sp=0&at=0'
    page2 = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
    tree2 = html.fromstring(page2.content)
    xpath='//*[@id="PaginacionSuperior"]/div/ul/li[6]/a'
    last=tree2.xpath(xpath)
    try:
        last=last[0]
    except:
        for i in range (1,5):
            xpath='//*[@id="PaginacionSuperior"]/div/ul/li['+str(6-i)+']/a'
            last=tree2.xpath(xpath)
            try:
                last=last[0]
                break
            except:
                continue
    try:
        last=last.attrib

        last=str(last)
        last=last.split('=')
        last=last[8]
        last=last.split(',')
        last=last[0]
        last=last[:-1]
        try:
            last=int(last)
        except:
            last=int(last[0])
    except:
        last=1
    print("[SPIVM] " + str(last))
    return last

def insertarPropiedad(propiedad):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO portalinmobiliario(id2,nombre,fechapublicacion,fechascrap,region,direccion,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,lat,lon,link)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nombre=%s,fechapublicacion=%s,fechascrap=%s,region=%s,direccion=%s,operacion=%s,tipo=%s,precio=%s,dormitorios=%s,banos=%s,metrosmin=%s,metrosmax=%s,estacionamientos=%s,lat=%s,lon=%s,link=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))

    mariadb_connection.commit()
    mariadb_connection.close()

def getBanned():
    sql="SELECT mail FROM baneados"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    baneados = cur.fetchall()
    mariadb_connection.close()
    return baneados

def insertarDueno(dueno):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO duenos(idProp,mail,esDueno)
             VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE mail=%s, esDueno=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (dueno))

    mariadb_connection.commit()
    mariadb_connection.close()

def insertarRemate(propiedad):
    #En caso de ser remate, inserta en tabla de remates
    sql = """INSERT INTO remates(id2,nombre,fechapublicacion,fechascrap,region,direccion,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,lat,lon,link)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nombre=%s,fechapublicacion=%s,fechascrap=%s,region=%s,direccion=%s,operacion=%s,tipo=%s,precio=%s,dormitorios=%s,banos=%s,metrosmin=%s,metrosmax=%s,estacionamientos=%s,lat=%s,lon=%s,link=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))

    mariadb_connection.commit()
    mariadb_connection.close()

def esDueno(mail):


    ban=getBanned()

    if mail in ban:
        return "no"

    elif("gmail" in mail) or ("hotmail" in mail) or ("yahoo" in mail) or ("vtr" in mail):
        if ("propiedad" not in mail) and ("corredor" not in mail) and ("corretaje" not in mail) and ("inmueble" not in mail) and ("inmobiliari" not in mail) and ("casa" not in mail) and ("departamento" not in mail) and ("consultor") not in mail:
            return "si"
        else:
            return "no"
    else:
        return "no"

def getInfo(subsites,desde,hasta,lista,faillista,op,tip,reg):

    for j in range(desde, hasta):
        try:
            page2 = requests.get(subsites[j], headers={'User-Agent': agentCreator.generateAgent()})
            tree2 = html.fromstring(page2.content)


        except:
            print("[SPIVM] fail")

        lastRange = 25
        for i in range(1,lastRange+3):

            global a
            codeSite =  '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(i) + ']/div[2]/div/div[1]/p[2]'
            nameSite =  '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(i) + ']/div[2]/div/div[1]/h4/a'
            priceSite = '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(i) + ']/div[2]/div/div[2]/p/span'
            meterSite = '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(i) + ']/div[2]/div/div[3]/p/span'
            stateSite =  '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(i) + ']/div[2]/div/div[1]/p[1]/span'

            code = tree2.xpath(codeSite)

            if len(code) == 0:
                codeSite = '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(
                    i) + ']/div[2]/div/div[1]/p[3]'
                '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[1]/div[2]/div/div[1]/p[3]'
                code = tree2.xpath(codeSite)
            name = tree2.xpath(nameSite)
            price = tree2.xpath(priceSite)
            meters = tree2.xpath(meterSite)
            state = tree2.xpath(stateSite)
            if len(code) > 0:
                aux = []
                code = (code[0]).text
                if ("Codigo" not in code) and ("Código" not in code):
                    codeSite = '//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div[' + str(
                        i) + ']/div[2]/div/div[1]/p[3]'
                    code = tree2.xpath(codeSite)
                    code = (code[0]).text

                try:
                    code = int(code[8:])

                except:
                    print("[SPIVM] fail")

                aux.append(code)

                newLink = str((name[0]).attrib)
                newLink = newLink[17:]
                newLink = newLink[:-4]
                newLink = 'http://www.portalinmobiliario.com/venta/' + newLink

                name = (name[0]).text
                price = (price[0]).text
                price = str(price)
                price = price[2:]

                try:

                    price = float(price.replace('.', ''))

                    if len(meters) > 0:
                        meters = meters[0].text
                    else:
                        meters = 'missing'
                    if '-' in meters:
                        meters = meters.split('-')
                        minMeters = (meters[0])[:-1]
                        maxMeters = (meters[1])[:-3]
                        maxMeters = maxMeters[1:]
                        minMeters = float(minMeters.replace(',','.'))
                        maxMeters = float(maxMeters.replace(',','.'))


                    elif 'missing' in meters:
                        minMeters = -1
                        maxMeters = -1
                    else:
                        meters = meters[:-3]
                        meters = float(meters.replace(',','.'))
                        minMeters = meters
                        maxMeters = meters

                except:
                    try:
                        l=faillista[-1]
                        l=l+1
                        faillista.append(l)
                        print ("[SPIVM] fails:"+str(l))
                    except:
                        l=1
                        print ("[SPIVM] fails (price or meters):"+str(l))
                        faillista.append(l)
                    print("[SPIVM] continued")
                    continue

                try:
                    page3 = requests.get(newLink, headers={'User-Agent': agentCreator.generateAgent()})
                    tree3 = html.fromstring(page3.content)
                except:
                    print("[SPIVM] fail")

                addresSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[1]/div[2]/div[1]/div/div/p[3]/span[1]'
                address = tree3.xpath(addresSite)
                if len(address) == 0:
                    addresSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[1]/p/span[1]'
                    address = tree3.xpath(addresSite)
                if len(address) == 0:
                    addresSite = '//*[@id="project-location"]/div/div/div[1]/div/div[1]/p/span[1]'
                    address = tree3.xpath(addresSite)
                if len(address) > 0:
                    try:
                        address = address[0].text
                    except AttributeError:
                        address = '-'
                else:
                    address = None

                latSite = '/html/head/meta[18]'
                lat = tree3.xpath(latSite)
                if len(lat) > 0:
                    lat = str((lat[0]).attrib).split(':')
                    lat = lat[3]
                    lat = (lat[2:])[:-2]

                    try:
                        lat = float(lat)
                    except:
                        try:
                            l=faillista[-1]
                            l=l+1
                            faillista.append(l)
                            print ("[SPIVM] fails:"+str(l))
                        except:
                            l=1
                            print ("[SPIVM] fails (lat):"+str(l))
                            faillista.append(l)
                        continue

                else:
                    lat = None

                lonSite = '/html/head/meta[19]'
                lon = tree3.xpath(lonSite)
                if len(lon) > 0:
                    lon = (((str((lon[0]).attrib).split(':'))[3])[2:])[:-2]
                    try:
                        lon= float(lon)
                    except:
                        try:
                            l=faillista[-1]
                            l=l+1
                            print ("[SPIVM] fails:"+str(l))
                            print (l)
                        except:
                            l=1
                            print ("[SPIVM] fails (lon):"+str(l))
                            faillista.append(l)
                        continue
                else:
                    lon = None

                dormSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[2]/p/text()[1]'
                dorms = tree3.xpath(dormSite)

                try:
                    if len(dorms) > 0:

                        dorms=str(dorms)
                        dorms=dorms[2]
                        dorms=float(dorms)
                    else:

                        dormSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[1]/div[2]/p/text()[1]'

                        dorms = tree3.xpath(dormSite)
                        if len(dorms) > 0:
                            dorms=str(dorms)
                            dorms=dorms[2]
                            dorms=float(dorms)
                        else:

                            dorms = None
                except AttributeError:

                    dorms = None

                bathSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[2]/div[2]/p/text()[2]'
                baths = tree3.xpath(bathSite)

                try:
                    if len(baths) > 0:
                        baths = str(baths)
                        baths = baths[2]
                        baths = float(baths)
                    else:
                        bathSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[1]/div[2]/p/text()[2]'
                        baths = tree3.xpath(bathSite)
                        if len(baths) > 0:
                            baths = str(baths)
                            baths = baths[2]
                            baths = float(baths)
                        else:

                            baths = None
                except AttributeError:

                    baths = None

                r = session.get(newLink)
                mails = []
                corredor="no"
                rtext=r.text
                if "empresas/ficha" in rtext:
                    #no es dueño
                    corredor="si"
                rtext=rtext.split(' ')

                for x,a in enumerate(rtext):
                    if 'emailVendedor' in a:
                        emailvendedor=rtext[x+2]
                        emailvendedor=emailvendedor.replace('\r\n','')
                        emailvendedor=emailvendedor.replace('"','')
                        dueno=[]
                        dueno.append(code)
                        dueno.append(emailvendedor)
                        if (corredor=="si"):
                            dueno.append("no")
                            dueno.append(emailvendedor)
                            dueno.append("no")
                        else:
                            dueno.append(esDueno(emailvendedor))
                            dueno.append(emailvendedor)
                            dueno.append(esDueno(emailvendedor))

                dateSite = '//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[1]/div[1]/div[2]/p[2]/strong'
                date = tree3.xpath(dateSite)
                if len(date) > 0:
                    date = date[0].text
                    date = date[11:]
                    dateSplit = date.split('-')
                    date = dateSplit[2]+'-'+dateSplit[1]+'-'+dateSplit[0]
                else:
                    date = None

                split = subsites[j].split('/')

                operacion = split[3]
                tipo = split[4]
                split2 = split[5].split('?')
                region = split2[0]

                estacionamientos=0
                texts=[]
                for p in range (1,20):
                    try:
                        path='//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[3]/div/div/text()['+str(p)+']'
                        texto=tree3.xpath(path)
                        texto=texto[0]
                        texto=str(texto)

                        texts.append(texto)

                    except:
                        continue


                remate=0
                for texto in texts:

                    if (('studio' in texto) or ('Studio' in texto) or ('STUDIO' in texto)):
                        if (('estudio' not in texto) or ('Estudio' not in texto) or ('ESTUDIO' not in texto)):
                            dorms=0

                    if (('fecha de remate' in texto) or ('Fecha de Remate' in texto) or ('FECHA DE REMATE' in texto) or ('Fecha de remate' in texto)or ('Fecha De Remate' in texto)):
                        remate=1
                    else:
                        remate=0

                    if 'Estacionamientos: 1' in texto:
                            estacionamientos=1
                            break
                    elif 'Estacionamientos: 2' in texto:
                        estacionamientos=2
                        break
                    elif 'Estacionamientos: 3' in texto:
                        estacionamientos=3
                        break
                    elif ('in Estacionamiento' in texto) or ('in estacionamiento' in texto) or ('IN ESTACIONAMIENTO' in texto) or ('IN estacionamiento' in texto) or ('IN Estacionamiento' in texto):
                        estacionamientos=0
                        break
                    elif ('stacionamiento: N' in texto) or ('stacionamiento: n' in texto) or ('STACIONAMIENTO: N' in texto) or ('STACIONAMIENTO: n' in texto) or ('stacionamientos: N' in texto) or ('stacionamientos: n' in texto) or ('STACIONAMIENTOS: N' in texto) or ('STACIONAMIENTOS: n' in texto):
                        estacionamientos=0
                        break
                    elif ('estacionamiento' in texto) or ('Estacionamiento' in texto) or ('ESTACIONAMIENTO' in texto):
                        estacionamientos=1
                        if (('INCLUYE' in texto) or ('Incluye' in texto) or ('incluye' in texto)) and (('ESTACIONAMIENTO' in texto) or ('Estacionamiento' in texto) or ('estacionamiento' in texto)):
                            if (('No' in texto) or ('NO' in texto) or ('no' in texto)):
                                estacionamientos=0
                            elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                                estacionamientos=0
                            else:
                                 estacionamientos=1

                        elif (('TIENE' in texto) or ('Tiene' in texto) or ('tiene' in texto)) and (('ESTACIONAMIENTO' in texto) or ('Estacionamiento' in texto) or ('estacionamiento' in texto)):
                            if (('No' in texto) or ('NO' in texto) or ('no' in texto)):
                                estacionamientos=0
                            elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                                estacionamientos=0
                            else:
                                 estacionamientos=1

                        elif ('Visita' in texto) or ('visita' in texto) or ('VISITA' in texto):
                             estacionamientos=0

                        #elif ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto):
                        else:
                            if (('Sin' in texto) or ('SIN' in texto) or ('sin' in texto)):
                                estacionamientos=0
                            #elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                                #estacionamientos=0
                            else:
                                 estacionamientos=1

                        break


                fechahoy = datetime.datetime.now()
                fechascrap=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)

                aux.append(name)
                aux.append(date)
                aux.append(fechascrap)
                aux.append(region)
                aux.append(address)
                aux.append(operacion)
                aux.append(tipo)
                aux.append(price)
                aux.append(dorms)
                aux.append(baths)
                aux.append(minMeters)
                aux.append(maxMeters)
                aux.append(estacionamientos)
                aux.append(lat)
                aux.append(lon)
                aux.append(newLink)
                aux.append(name)
                aux.append(date)
                aux.append(fechascrap)
                aux.append(region)
                aux.append(address)
                aux.append(operacion)
                aux.append(tipo)
                aux.append(price)
                aux.append(dorms)
                aux.append(baths)
                aux.append(minMeters)
                aux.append(maxMeters)
                aux.append(estacionamientos)
                aux.append(lat)
                aux.append(lon)
                aux.append(newLink)

                lista=lista+1
                print ("[SPIVM] "+ str(tipo) + "s en "+operacion+" registradas/os en: "+str(region)+": "+str(lista))
                time.sleep(random.uniform(0,0.5))

                try:
                    insertarDueno(dueno)
                except:
                    abdcedf=0


                if remate==0:
                    try:
                        insertarPropiedad(aux)
                    except:
                        continue
                else:
                    insertarRemate(aux)

                actualizar_checker(op,tip,reg,j)

def scrap(d,h,operacion,tipo,region,lista,faillista):

    link = "http://www.portalinmobiliario.com/"+str(operacion)+"/"+str(tipo)+"/"+str(region)+"?tp=6&op=2&ca=2&ts=1&dd=0&dh=6&bd=0&bh=6&or=&mn=1&sf=0&sp=0&pg=1"

    try:
        page2 = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        tree2 = html.fromstring(page2.content)
    except:
        print("[SPIVM] fail")
    paginas = tree2.xpath('//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[1]/div[1]/div/div/text()[1]')

    if len(paginas) == 0:
        return

    pagsplit = (str(paginas[0]).split())[2]
    nrOfPubs = int(pagsplit.replace(".", ""))

    nrOfPbsPerPage = 25

    nrPages = math.ceil(nrOfPubs/nrOfPbsPerPage)

    subsites = []
    subsiteBasicUrl = (link)[:-1]
    for i in range(1,nrPages+1):
        subsites.append(subsiteBasicUrl + str(i))

    getInfo(subsites,d,h,lista,faillista,operacion,tipo,region)

def Main(tipoRec="departamento",operacionRec="venta", regionRec="metropolitana",pagRec=0,isRecovery=False):


    #Obtener proxies
    proxies=get_proxiestextweb()
    proxy_pool=cycle(proxies)

    while True:

        proxi=next(proxy_pool)
        lista=0
        faillista=[]
        print("[SPIVDM] Running scraper for: "+"venta"+" "+"departamento"+" "+"metropolitana")

        last=getLast("venta","departamento","metropolitana",proxi)
        print("[SPIVDM]" + str(last))

        if isRecovery:
            firstPage = pagRec
            isRecovery = False
        else:
            firstPage=0

        scrap(firstPage,last,"venta","departamento","metropolitana",lista,faillista)
        print("[SPIVDM] scraper ran")



    print("[SPIVDM] Main Complete")

if __name__=="__main__":
    Main()
