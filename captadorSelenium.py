import datetime
import random
import requests
import time
from lxml import html
import uf
import contactadorPortalMercadoLibre as contactador
uf = uf.getUf()

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

body1 = "Hola!\n\n"
body1 += "Te escribo por tu publicación en Portalinmobiliario \n\n"


body1 += "Mi nombre es Carolina, trabajo en Vendetudepto.cl, y como promoción de lanzamiento, estamos ofreciendo servicios Totalmente Gratuitos de difusión inmobiliaria.\n\n"
body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad.\n\n"

body1 += "El servicio incluye publicaciones con cuentas pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión de visitas. Como te mencioné anteriormente, esto no tiene absolutamente ningún costo para ti.\n"
body1 += "Además, realizamos el acompañamiento hasta la firma final de compraventa o de arriendo de la propiedad.\n\n"
body1 += "Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo carolina@vendetudepto.cl (precio, características, horarios de visita, fotografías, etc), y con gusto asignaremos un corredor para tu propiedad. Junto con esto, rogamos enviarnos tu número de contacto.\n\n"
body1 += "Ante cualquier duda, por favor escríbeme al correo o a nuestro WhatsApp +569 8936 6288.\n"
body1 += "De antemano muchas gracias por tu tiempo,\n\n"
body1 += "Saludos cordiales,\n\n"
body1 += "Carolina, \n"
body1 += "www.vendetudepto.cl\n\n"
body1 += "PD: Si usted es corredor de propiedades, rogamos indicar si la propiedad está disponible para canje."

headerList = [headers1,headers2,headers3]


dormitorios = ["1-dormitorio",
                "2-dormitorios",
                "3-dormitorios",
                "sin-dormitorios",
                "mas-de-4-dormitorios"]
banos = ["_Banos_2",
          "_Banos_3",
          "_Banos_4",
          "_Banos_1",
          "_Banos_5-o-mas"]

comunas = ["lo-barnechea","las-condes","la-reina","recoleta","independencia","estacion-central",
           "san-miguel","nunoa","providencia","macul","quinta-normal","san-joaquin","vina-del-mar","valparaiso","concon",]
regiones=["metropolitana","valparaiso"]
operaciones = ["arriendo","venta"]
tipos = ["departamento"]

pages = range(1,2050,50)

def obtenerBodegas(texto):
    bodegas=0

    texto=texto.lower()

    visitas=['bodega de visita','bodegas de visita','bodega visita','bodegas visita','bodega para visita', 'bodegas para visita']
    for vis in visitas:
        if(vis in texto):
            texto=texto.replace(vis,'')

    if 'bodegas: 0' in texto:
        bodegas=0
    elif 'bodegas: 1' in texto:
        bodegas=1
    elif 'bodegas: 2' in texto:
        bodegas=2
    elif 'bodegas: 3' in texto:
        bodegas=3
    elif ('in bodega' in texto):
        bodegas=0
    elif ('bodega: n' in texto):
        bodegas=0
    elif ('bodega' in texto):
        if ('incluye bodega' in texto):
            if ('no incluye bodega' in texto):
                bodegas=0
            elif ('ni incluye bodega' in texto):
                bodegas=0
            elif ('tampoco incluye bodega' in texto):
                bodegas=0
            else:
                 bodegas=1

        elif ('tiene bodega' in texto):
            if ('no tiene bodega' in texto):
                bodegas=0
            elif ('ni tiene bodega' in texto):
                bodegas=0
            else:
                 bodegas=1

        elif ('con bodega' in texto):
            if ('cuenta con bodega' in texto):
                if ('no cuenta con bodega' in texto):
                    bodegas=0
                elif ('ni cuenta con bodega' in texto):
                    bodegas=0
                elif ('tampoco cuenta con bodega' in texto):
                    bodegas=0
                else:
                    bodegas=1
            elif ('viene con bodega' in texto):
                if ('no viene con bodega' in texto):
                    bodegas=0
                elif ('ni viene con bodega' in texto):
                    bodegas=0
                else:
                    bodegas=1
            else:
                bodegas=1
        elif (('ni bodega' in texto) or ('no bodega' in texto)):
            bodegas=0

        elif (('sin bodega' in texto)):
            bodegas=0

        elif ('tiene bodega' in texto):
            if ('no tiene bodega' in texto):
                bodegas=0
            elif ('ni tiene bodega' in texto):
                bodegas=0
            else:
                bodegas=1
        elif ('posee bodega' in texto):
            if ('no posee bodega' in texto):
                bodegas=0
            elif ('ni posee bodega' in texto):
                bodegas=0
            else:
                bodegas=1

        else:
            bodegas=1
    return bodegas

def obtenerEstacionamientos(texto):
    estacionamientos=0

    texto=texto.lower()

    visitas=['estacionamiento de visita','estacionamientos de visita','estacionamiento visita','estacionamientos visita','estacionamiento para visita', 'estacionamientos para visita']
    for vis in visitas:
        if(vis in texto):
            texto=texto.replace(vis,'')

    if 'estacionamientos: 0' in texto:
        estacionamientos=0
    elif 'estacionamientos: 1' in texto:
        estacionamientos=1
    elif 'estacionamientos: 2' in texto:
        estacionamientos=2
    elif 'estacionamientos: 3' in texto:
        estacionamientos=3
    elif ('in estacionamiento' in texto):
        estacionamientos=0
    elif ('estacionamiento: n' in texto):
        estacionamientos=0
    elif ('estacionamiento' in texto):
        if ('incluye estacionamiento' in texto):
            if ('no incluye estacionamiento' in texto):
                estacionamientos=0
            elif ('ni incluye estacionamiento' in texto):
                estacionamientos=0
            elif ('tampoco incluye estacionamiento' in texto):
                estacionamientos=0
            else:
                 estacionamientos=1

        elif ('tiene estacionamiento' in texto):
            if ('no tiene estacionamiento' in texto):
                estacionamientos=0
            elif ('ni tiene estacionamiento' in texto):
                estacionamientos=0
            else:
                 estacionamientos=1

        elif ('con estacionamiento' in texto):
            if ('cuenta con estacionamiento' in texto):
                if ('no cuenta con estacionamiento' in texto):
                    estacionamientos=0
                elif ('ni cuenta con estacionamiento' in texto):
                    estacionamientos=0
                elif ('tampoco cuenta con estacionamiento' in texto):
                    estacionamientos=0
                else:
                    estacionamientos=1
            elif ('viene con estacionamiento' in texto):
                if ('no viene con estacionamiento' in texto):
                    estacionamientos=0
                elif ('ni viene con estacionamiento' in texto):
                    estacionamientos=0
                else:
                    estacionamientos=1
            else:
                estacionamientos=1
        elif (('ni estacionamiento' in texto) or ('no estacionamiento' in texto)):
            estacionamientos=0

        elif (('sin estacionamiento' in texto)):
            estacionamientos=0

        elif ('tiene estacionamiento' in texto):
            if ('no tiene estacionamiento' in texto):
                estacionamientos=0
            elif ('ni tiene estacionamiento' in texto):
                estacionamientos=0
            else:
                estacionamientos=1
        elif ('posee estacionamiento' in texto):
            if ('no posee estacionamiento' in texto):
                estacionamientos=0
            elif ('ni posee estacionamiento' in texto):
                estacionamientos=0
            else:
                estacionamientos=1

        else:
            estacionamientos=1


    return estacionamientos

def scrap(linkList,region,operacion,comuna,tipo,hoja,driver,nrContactados):

    contactados = cargarContactados()
    headerIndex = 0

    for i,link in enumerate(linkList):

        print("[contactador] "+str(i+1+hoja) + " - " + str(region) + " - " + str(comuna) + " - "+str(operacion) + " - " +
              str(tipo))

        time.sleep(random.randint(1,3))
        try:
            request = requests.get(link, headers=headerList[headerIndex])
        except:
            time.sleep(random.randint(60,90))
            request = requests.get(link, headers=headerList[headerIndex])
        #headerIndex += 1
        #headerIndex = headerIndex % len(headerList)
        try:
            tree = html.fromstring(request.content)
        except:
            print("Error al crear tree.")
            continue

        try:
            code=int(link.split('/')[6].split('-')[0])

        except Exception as err:
            print("Error al sacar codigo")
            continue

        # verificar si es dueño y crear objeto dueño
        agency_path = '//*[@id="real_estate_agency"]'

        agency = tree.xpath(agency_path)

        esPropietario = False
        if len(agency) == 0:

            name_xpath = '//*[@id="root-app"]/div/div[1]/div[2]/section[1]/p[3]/span'
            name = tree.xpath(name_xpath)
            if len(name) > 0:
                name = (name[0]).text

            if "orredor" in name or "ropiedad" in name or "nmobilia" in name:
                esPropietario = False

            else:
                descr_path = '//*[@id="description-includes"]/div/p/text()[1]'
                descr_path2 = '//*[@id="description-includes"]/div/p/text()'

                descripcion = tree.xpath(descr_path)
                if len(descripcion) == 0:
                    descripcion = tree.xpath(descr_path2)

                if len(descripcion) != 0:
                    descripcion = descripcion[0]

                tags_duenos=["in comision","in comisión","dueñ","Dueñ","in corredor","irect"]
                tags_corredores=["omisión:","omision","orredor"]

                esPropietario = True

                for tag in tags_corredores:
                    if tag in descripcion:
                        esPropietario = False

                for tag in tags_duenos:
                    if tag in descripcion:
                        esPropietario = True

        code = str(code)
        if esPropietario:
            if code not in contactados:
                print("Candidato encontrado. Contactando.")
                contactador.contactPublication(driver,link,body1)
                updateArchivoContactados([code])
                nrContactados += 1
                if nrContactados %19==0:
                    time.sleep(3600)

            else:
                print("Código " + str(code) + " estaba en lista de contactados")
        else:
            print("No es propietario.")


        return nrContactados



def updateArchivoContactados(lista):
    f=open("contactados.txt", "a+")
    for e in lista:
        f.write(str(e)+"\n")
    f.close()

def cargarContactados():
    f=open("contactados.txt", "r")
    contents = f.read()
    list = contents.split("\n")
    f.close()
    return list[:-1]

def main():
    driver = contactador.initialize()
    #sacar esto!
    nrContactados = 0

    headerIndex = 0
    for region in regiones:
        for comuna in comunas:
            for operacion in operaciones:
                for tipo in tipos:
                    for dormitorio in dormitorios:

                        for bano in banos:
                            for page in pages:
                                time.sleep(random.randint(5,7))
                                if page==1:
                                    page=0
                                link = "https://www.portalinmobiliario.com/"+operacion+"/"+tipo+"/propiedades-usadas/"+dormitorio+"/"+comuna+"-"+region+"/_Desde_"+str(page)+bano
                                print("Sacando links de "+link)
                                request = requests.get(link, headers = headerList[headerIndex])

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
                                try:
                                    nrContactados += scrap(linkList=resultLinkList,region=region,operacion=operacion,comuna=comuna,
                                      tipo=tipo,hoja=page,driver=driver,nrContactados=nrContactados)
                                except:
                                    pass


def contactar(potencialesContactos,idsPotencialesContactos):
    contactador.main(potencialesContactos)
    updateArchivoContactados(idsPotencialesContactos)

if __name__ == "__main__":
    main()
