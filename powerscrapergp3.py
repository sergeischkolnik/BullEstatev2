from lxml import html
import requests
import datetime
from time import sleep
from itertools import cycle
from threading import Thread
import pymysql as mysql

def llenarLista(lista,removelist,desde,hasta):
    for i in range(desde,hasta):
        if i%1000000==0:
            print(str(int(100*(((i-1000000)/4000000))))+"%")
        if not (binarySearch(removelist,i)):
            lista.append(i)

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def insertargpscrap(listai,mariadb_connection):
    sql = """INSERT INTO goplaceit_scraped(lista)
             VALUES(%s) ON DUPLICATE KEY UPDATE lista=%s"""

    cur = mariadb_connection.cursor()

    cur.execute(sql, (listai))
    mariadb_connection.commit()


def insertarPropiedadgp(propiedad,mariadb_connection):
    sql = """INSERT INTO goplaceit(id2,nombre,fechapublicacion,fechascrap,region,provincia,comuna,operacion,tipo,precio,moneda,dormitorios,banos,metrosmin,metrosmax,gastoscomunes,estacionamientos,ano,piso,orientacion,amoblado,antiguedad,dueno,lat,lon,link,disponibilidad)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nombre=%s,fechapublicacion=%s,fechascrap=%s,region=%s,provincia=%s,comuna=%s,operacion=%s,tipo=%s,precio=%s,moneda=%s,dormitorios=%s,banos=%s,metrosmin=%s,metrosmax=%s,gastoscomunes=%s,estacionamientos=%s,ano=%s,piso=%s,orientacion=%s,amoblado=%s,antiguedad=%s,dueno=%s,lat=%s,lon=%s,link=%s,disponibilidad=%s"""

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))
    mariadb_connection.commit()


def remove(desde,hasta,removelist):
    sublista=[]
    for i in range(desde,hasta):
        if i in removelist:
            continue
        else:
            sublista.append(i)
    return sublista

def fromgpscrap():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='goplaceit')
    cur = mariadb_connection.cursor()
    sql = "SELECT lista FROM goplaceit_scraped"
    cur.execute(sql)
    tupla = cur.fetchall()
    removelist = []
    for i in tupla:
        i = i[0]
        removelist.append(i)
    return removelist

# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = html.fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr'):
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies

def get_proxiesb():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    parser = html.fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def get_proxiesc():
    url = 'https://www.socks-proxy.net/'
    response = requests.get(url)
    parser = html.fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def get_proxiestextweb():
    url="https://proxyscrape.com/proxies/HTTP_Working_Proxies.txt"
    proxies=set()
    response=requests.get(url)
    ip=response.text.split('\r\n')
    for proxy in ip:
            proxies.add(proxy)
    return proxies


def get_proxies2():
    url = 'https://us-proxy.org/'
    response = requests.get(url)
    page = html.fromstring(response.content)
    proxies=set()
    for i in range (1,200):
        ipxpath='//*[@id="proxylisttable"]/tbody/tr['+str(i)+']/td[1]'
        ip=page.xpath(ipxpath)
        portxpath='//*[@id="proxylisttable"]/tbody/tr['+str(i)+']/td[2]'
        port=page.xpath(portxpath)
        proxy = ip[0].text+":"+port[0].text
        proxies.add(proxy)
    return proxies


def get_proxies3():
    link = "https://www.duplichecker.com/free-proxy-list.php"
    r = requests.get(link)
    tree = html.fromstring(r.content)
    data = tree.xpath('//*[@id="body"]/div/div/div[4]/div/form/div/div/div/textarea')
    proxies=set()
    data = data[0].text
    data = data.split("\n")
    for i in data:
        proxies.add(i)
    return proxies

def get_proxies4():
    proxies=set()

    for i in range(0,39):
        link="http://www.workingproxies.org/?page="+str(i)

        page3 = requests.get(link)
        tree3 = html.fromstring(page3.content)
        for j in range (1,50):
            ip=tree3.xpath('/html/body/div[2]/table/tbody/tr['+str(j)+']/td[1]')
            port=tree3.xpath('/html/body/div[2]/table/tbody/tr['+str(j)+']/td[2]')
            proxy=str(ip[0].text)+":"+str(port[0].text)
            proxies.add(proxy)

    return(proxies)

def get_proxies5():

    proxies=set()


    link="http://fineproxy.org/eng/fresh-proxies"

    page3 = requests.get(link)
    tree3 = html.fromstring(page3.content)
    page2=page3.text

    page2=page2.split('/')
    page1=[]
    for i in page2:
        if (("br" in i) and("." in i)):
            i=i[2:-4]
            proxies.add(i)

    return(proxies)

def get_proxiestxt():
    proxies=set()
    strPath = "Proxy List.txt"
    f = open(strPath)
    strText = f.read()
    ip=strText.split('\n')
    for i in ip:
        proxies.add(i)
    return proxies

def get_proxies6():
    proxies=set()
    url = 'http://www.httptunnel.ge/ProxyListForFree.aspx'
    response = requests.get(url)
    parser = html.fromstring(response.text)
    for i in range (2,145):
        if i<=9:
            num="0"+str(i)

        else:
            num=str(i)
        ip=parser.xpath('//*[@id="ctl00_ContentPlaceHolder1_GridViewNEW_ctl'+num+'_HyperLink2"]')
        ip=ip[0].text
        proxies.add(ip)

    return(proxies)

def scrapergp(link,proxy,succes,lista_i,mariadb_connection):
    activa=1
    aux=[]

    try:
        page3 = requests.get(link, timeout=30, proxies={"http": proxy, "https": proxy})
        tree3 = html.fromstring(page3.content)
    except:
        activa=0

    if (activa==1):
        #Xpaths
        #Pais
        try:
            pais=tree3.xpath('//*[@id="info"]/div[4]/div/a/span[1]')
            pais=str(pais[0].text)
        except:
            activa=0

        if (pais!="Chile") and (activa==1):
            #print("NOT CHILE")
            activa=2
            succes.append(lista_i)

    if(activa==1):

        # nombre
        name = tree3.xpath('//*[@id="info"]/div[4]/h1')
        name = str(name[0].text)

        #Disponibilidad
        try:
            disponibilidad=tree3.xpath('/html/body/div[2]/div[1]/div/text()')
            disponibilidad=str(disponibilidad[0])
        except:
            disponibilidad=('Propiedad disponible')

        #Fecha Publicacion

        try:
            fechapublicacion = tree3.xpath('//*[@id="info"]/div[5]')
            fechapublicacion=str(fechapublicacion[0].text)
            fechapublicacion=fechapublicacion.split(' ')
            fechapublicacion=str(fechapublicacion[2])
            fechapublicacion=fechapublicacion.split('/')
            year=(str(fechapublicacion[2]))

            if len(year)>=5:
                year=year[:-1]

            fechapublicacion=year+'-'+str(fechapublicacion[1])+'-'+str(fechapublicacion[0])
        except:
            activa=0
            succes.append(lista_i)
        #Fecha scrap
        fechascrap=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)

        #Region
        try:
            region= tree3.xpath('//*[@id="info"]/div[4]/div/div/a[1]/span')
            region=str(region[0].text)
        except:
            if (activa==1):
                succes.append(lista_i)
            activa = 0

        #Provincia
        try:
            provincia= tree3.xpath('//*[@id="info"]/div[4]/div/div/a[2]/span')
            provincia=str(provincia[0].text)
        except:
            provincia=None

        #Comuna
        try:
            comuna= tree3.xpath('//*[@id="info"]/div[4]/div/div/a[3]/span')
            comuna=str(comuna[0].text)
        except:
            comuna=None
        #latitud
        lat=tree3.xpath('//*[@id="info"]/div[3]/span[1]')
        lat=float(lat[0].text)

        #longitud
        lon = tree3.xpath('//*[@id="info"]/div[3]/span[2]')
        lon=float(lon[0].text)

        #Operacion y tipo
        try:
            operacion=tree3.xpath('//*[@id="info"]/div[6]/div/div[1]/span')
            operacion=str(operacion[0].text)

            if("Casa" in operacion):
                if("Venta" in operacion):
                    tipo="casa"
                    operacion="venta"

                else:
                    tipo = "casa"
                    operacion = "arriendo"

            elif ("Departamento" in operacion):
                if ("Venta" in operacion):
                    tipo = "departamento"
                    operacion = "venta"

                else:
                    tipo = "departamento"
                    operacion = "arriendo"

            else:
                if ("venta" in operacion):
                    tipo = "oficina"
                    operacion = "venta"

                else:
                    tipo = "oficina"
                    operacion = "arriendo"
        except:
            if (activa==1):
                succes.append(lista_i)
            activa=0


    if (activa==1):
        precio = None
        moneda = None
        dormitorios = None
        banos = None
        metrosmin = None
        metrosmax = None
        dueno = None
        estacionamientos = None
        amoblado = None
        ano = None
        antiguedad = None
        id2 = None
        gastoscomunes = None
        piso = None
        orientacion = None


        for k in range(2,25):
            try:

                #indicador:
                indicador = tree3.xpath('//*[@id="info"]/div[6]/div/div[' + str(k) + ']/span')
                indicador=str(indicador[0].text)


                if (("Precio" in indicador) and ("por" not in indicador)):
                    #Precio

                    precio=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    precio=str(precio[0].text)
                    preciob = precio.split(' ')
                    precio= str(preciob[2])
                    precio=precio.replace('.','')
                    precio = precio.replace(',','.')
                    precio=float(precio)

                    #moneda

                    if('UF' in str(preciob[1])):
                        moneda="UF"
                    else:
                        moneda="CLP"

                elif (("habitación" in indicador) or ("habitaciones" in indicador)):
                    #Dormitorios

                    dormitorios=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    dormitorios = str(dormitorios[0].text)
                    dormitorios=dormitorios.split(' ')
                    dormitorios=int(dormitorios[0])
                    continue

                elif ("baño" in indicador) or ("baÃ±o" in indicador):
                    #Baños

                    banos=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    banos=str(banos[0].text)
                    banos = banos.split(' ')
                    banos = int(banos[0])
                    continue

                elif ("útiles" in indicador):
                    #MetrosMin

                    metrosmin=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    metrosmin = str(metrosmin[0].text)
                    metrosmin = metrosmin.split(' ')
                    metrosmin = float(metrosmin[0])
                    continue

                elif ("totales" in indicador):
                    #MetrosMax

                    metrosmax=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    metrosmax = str(metrosmax[0].text)
                    metrosmax = metrosmax.split(' ')
                    metrosmax = float(metrosmax[0])
                    continue

                elif ("dueño" in indicador):
                    # Amoblado

                    dueno= tree3.xpath('//*[@id="info"]/div[6]/div/div[' + str(k) + ']/span')
                    dueno = str(dueno[0].text)
                    dueno=dueno.split(' ')
                    dueno=str(dueno[3])
                    continue

                elif ("estacionamientos" in indicador):
                    #Estacionamientos

                    estacionamientos=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    estacionamientos = str(estacionamientos[0].text)
                    estacionamientos=estacionamientos.split(' ')
                    estacionamientos= int(estacionamientos[0])
                    continue

                elif ("amoblado" in indicador):
                    #Amoblado

                    amoblado=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    amoblado = str(amoblado[0].text)
                    continue

                elif ("Año" in indicador) and ("baño" not in indicador):
                    #Año

                    ano=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    ano = str(ano[0].text)
                    ano= ano.split(' ')
                    ano= int(ano[1])
                    continue

                elif ("Antigüedad" in indicador) or ("AntigÃ¼edad" in indicador):
                    #Antiguedad

                    antiguedad=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    antiguedad = str(antiguedad[0].text)
                    antiguedad = antiguedad.split(' ')
                    antiguedad = str(antiguedad[1])
                    continue

                elif ("Código" in indicador) and ("empresa" not in indicador):
                    #Id2

                    id2=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    id2 = str(id2[0].text)
                    id2 = id2.split(' ')
                    id2 = int(id2[2])
                    continue

                elif ("Comunes" in indicador):
                    #GastosComunes

                    gastoscomunes=tree3.xpath('//*[@id="info"]/div[6]/div/div['+str(k)+']/span')
                    gastoscomunes = str(gastoscomunes[0].text)
                    gastoscomunes = gastoscomunes.split(' ')
                    gastoscomunes = str(gastoscomunes[3])
                    gastoscomunes = gastoscomunes.replace(".",'')
                    gastoscomunes = gastoscomunes.replace(",",'.')
                    float(gastoscomunes)
                    continue

                elif ("Piso" in indicador):
                    # Piso

                    piso = tree3.xpath('//*[@id="info"]/div[6]/div/div[' + str(k) + ']/span')
                    piso = str(piso[0].text)
                    piso = piso.split(' ')

                    if ("/" in piso[1]):
                        pisob=piso[1].split("/")
                        piso=int(pisob[0])
                    elif ("," in piso[1]):
                        pisob = piso[1].split(",")
                        piso = int(pisob[0])
                    elif ("-" in piso[1]):
                        pisob = piso[1].split("-")
                        piso = int(pisob[0])
                    else:
                        piso = int(piso[1])
                    continue

                elif ("Orientación" in indicador):
                    # Orientacion

                    orientacion = tree3.xpath('//*[@id="info"]/div[6]/div/div[' + str(k) + ']/span')
                    orientacion = str(orientacion[0].text)
                    orientacion = orientacion.split(' ')
                    orientacion = str(orientacion[1])
                    continue

                else:
                    continue


            except:
                continue
        #print("appending")
        aux.append(id2)
        aux.append(name)
        aux.append(fechapublicacion)
        aux.append(fechascrap)
        aux.append(region)
        aux.append(provincia)
        aux.append(comuna)
        aux.append(operacion)
        aux.append(tipo)
        aux.append(precio)
        aux.append(moneda)
        aux.append(dormitorios)
        aux.append(banos)
        aux.append(metrosmin)
        aux.append(metrosmax)
        aux.append(gastoscomunes)
        aux.append(estacionamientos)
        aux.append(ano)
        aux.append(piso)
        aux.append(orientacion)
        aux.append(amoblado)
        aux.append(antiguedad)
        aux.append(dueno)
        aux.append(lat)
        aux.append(lon)
        aux.append(link)
        aux.append(disponibilidad)
        aux.append(name)
        aux.append(fechapublicacion)
        aux.append(fechascrap)
        aux.append(region)
        aux.append(provincia)
        aux.append(comuna)
        aux.append(operacion)
        aux.append(tipo)
        aux.append(precio)
        aux.append(moneda)
        aux.append(dormitorios)
        aux.append(banos)
        aux.append(metrosmin)
        aux.append(metrosmax)
        aux.append(gastoscomunes)
        aux.append(estacionamientos)
        aux.append(ano)
        aux.append(piso)
        aux.append(orientacion)
        aux.append(amoblado)
        aux.append(antiguedad)
        aux.append(dueno)
        aux.append(lat)
        aux.append(lon)
        aux.append(link)
        aux.append(disponibilidad)
        insertarPropiedadgp(aux,mariadb_connection)

        #print(str(j)+"/"+str(z))
        #print("thread "+str(thread)+" completed")
        succes.append(lista_i)




contador=0
threadList=[]
lista=list(range(1000000,5000000))
j=0
print("Collecting remove list")
removelist=fromgpscrap()
removelist.sort()
lista=[]


print("Removing elements")
threadRemove=[]


llenarLista(lista,removelist,1000000,5000000)

# lenremove=len(removelist)/1000
# lenremove=int(lenremove)
# remcount=0
# for r in removelist:
#     lista.remove(r)
#     remcount=remcount+1
#     if remcount%1000==0:
#         print(str(remcount)+"/"+str(len(removelist)))



# for r in range (0,lenremove):
#     rem = Thread(target=remove, args=(lista,removelist,r))
#     try:
#         rem.start()
#         print("thread "+str(rem)+" started")
#         threadRemove.append(rem)
#     except:
#         continue
#
#
# for i,rem in enumerate(threadRemove):
#     rem.join()

print(str(len(removelist))+" elements removed")
print(len(lista))
while len(lista)!=0:
    fechahoy = datetime.datetime.now()
    contador=contador+1
    print("Ciclo: "+str(contador)+" con fecha y hora: "+str(fechahoy))
    #proxies=get_proxies()
    #proxiestxt=get_proxiestxt()
    #proxiesb = get_proxiesb()
    #proxiesc = get_proxiesc()
    #proxies2 = get_proxies2()
    #proxies3 = get_proxies3()
    #proxies4 = get_proxies4()
    #proxies5 = get_proxies5()
    #proxies6 = get_proxies6()
    proxies=get_proxiestextweb()
    #proxies = proxies.union(proxies2)
    ##proxies = proxies.union(proxies3)
    #proxies = proxies.union(proxies4)
    #proxies=proxies.union(proxies5)
    #proxies=proxies.union(proxiesb)
    #proxies=proxies.union(proxiesc)
    #proxies=proxies.union(proxiestxt)
    #proxies = proxies.union(proxies6)
    #proxies = proxies.union(proxies7)



    print(len(proxies))
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='goplaceit')
    proxy_pool = cycle(proxies)
    succes = []
    if (j+len(proxies)>len(lista)):
        j=0

    for i,proxy in enumerate (proxies):


        proxi=next(proxy_pool)

        link = "https://www.goplaceit.com/cl/propiedad/arriendo/departamento/vitacura/" + str(lista[i+j])
        t = Thread(target=scrapergp, args=(link, proxi, succes,lista[i+j],mariadb_connection))

        try:
            t.start()
            threadList.append(t)
        except:
            continue
        #print(lista[i])
    for i, t in enumerate(threadList):
        t.join()

    print(j)
    j=j+len(proxies)
    for suc in succes:
        #print(suc)
        listai=[]
        listai.append(suc)
        listai.append(suc)
        insertargpscrap(listai,mariadb_connection)
        lista.remove(int(suc))
    print("faltan: "+str(len(lista)))
    mariadb_connection.close()
    sleep(1.5)

