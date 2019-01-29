import datetime
import json
import random
import time
import agentCreator
from itertools import cycle
import insertToctoc
import requests
from random import shuffle
import pymysql as mysql


print(str(datetime.datetime.now()))

def get_proxiestextweb():
    url="https://proxyscrape.com/api?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    proxies=set()
    response=requests.get(url)
    ip=response.text.split('\r\n')
    for proxy in ip:
            proxies.add(proxy)
    return proxies

def getScrapedList():
    sql = "SELECT id FROM propiedades"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    tupla = cur.fetchall()
    mariadb_connection.close()
    return tupla

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

proxies=get_proxiestextweb()
proxy_pool = cycle(proxies)


x = [i for i in range(1000000)]
shuffle(x)

for id in x:
    proxi=next(proxy_pool)
    print(proxi)
    headers = {
    'cookie': 'X-DATA=2f5b2813-edf8-4b34-b07f-4087d288447f; NPS_93546e30_last_seen=1547558386874; _ga=GA1.2.989405458.1547558387; _gid=GA1.2.729091738.1547558387; NPS_93546e30_throttle=1547561987573; _fbp=fb.1.1547558388537.186150725; __RequestVerificationToken=86oRqQRziKy8hobVQw-bVcKUULRhKk0hFAUed5-63LKGrmXRJRKA0crNEPPaQTuaiiSjG9--AbVeffGENLIzkSOx8Hib95IdE4zhQsVcxuc1; optimizelyEndUserId=oeu1547558412070r0.6528189885507383; optimizelySegments=^%^7B^%^222204271535^%^22^%^3A^%^22gc^%^22^%^2C^%^222215970531^%^22^%^3A^%^22false^%^22^%^2C^%^222232940041^%^22^%^3A^%^22direct^%^22^%^7D; optimizelyBuckets=^%^7B^%^7D; __insp_wid=2107690165; __insp_slim=1547560739491; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudG9jdG9jLmNvbS9wcm9waWVkYWRlcy92aXZpZW5kYS9kZXBhcnRhbWVudG8vbGFzLWNvbmRlcy9jYW1pbm8tc2FuLWZyYW5jaXNjby1kZS1hc2lzLTExODAvNzI2MDE^%^3D; __insp_targlpt=VG9kYSBwcm9waWVkYWQgdGllbmUgc3UgcHJlY2lv; __insp_norec_sess=true; __atuvc=2^%^7C3; __atuvs=5c3de724c5463937000; X-DATA-NPSW=^{^\\^CantidadVisitas^\\^:1,^\\^FechaCreacion^\\^:^\\^2019-01-15T10:19:40.6966909-03:00^\\^,^\\^FechaUltimoIngreso^\\^:^\\^2019-01-15T11:02:06.4051203-03:00^\\^,^\\^Detalles^\\^:^[^{^\\^TipoVistaNPS^\\^:1,^\\^Cantidad^\\^:1,^\\^FechaUltimoIngreso^\\^:^\\^2019-01-15T10:19:40.6966909-03:00^\\^^},^{^\\^TipoVistaNPS^\\^:2,^\\^Cantidad^\\^:1,^\\^FechaUltimoIngreso^\\^:^\\^2019-01-15T10:20:09.9355287-03:00^\\^^},^{^\\^TipoVistaNPS^\\^:3,^\\^Cantidad^\\^:5,^\\^FechaUltimoIngreso^\\^:^\\^2019-01-15T11:02:06.4051203-03:00^\\^^}^]^}; _gat=1; mp_29ae90688062e4e2e6d80b475cef8685_mixpanel=^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^2216851ab60b688d-08d1095668adbc-b781636-15f900-16851ab60b745d^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^20^%^2216851ab60b688d-08d1095668adbc-b781636-15f900-16851ab60b745d^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fwww.toctoc.com^%^2F^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22www.toctoc.com^%^22^%^7D; optimizelyPendingLogEvents=^%^5B^%^5D',
    'x-xsrf-token': 'Ci7HAoA5M9U6itfuSvADh8YKudxIkLpWi4s_UMi7fMAMicuFnbjTdo2hgaPih-aOvxqO-LFBmNRURWRjnaikN7MeqzGnkuf7zGgiBzNEjXY1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9',
    'user-agent': agentCreator.generateAgent(),
    'accept': '*/*',
    'referer': 'https://www.toctoc.com/propiedades/vivienda/departamento/las-condes/camino-san-francisco-de-asis-1180/72601',
    'authority': 'www.toctoc.com',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = (
        ('id', id),
    )

    try:
        response = requests.get('https://www.toctoc.com/api/propiedades/bienRaiz/vivienda', headers=headers, params=params, proxies={"http": proxi, "https": proxi}, timeout=20)

    except:
        continue
    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://www.toctoc.com/api/propiedades/bienRaiz/vivienda?id=72601', headers=headers)


    json_data = json.loads(response.text)


    bien = json_data['BienRaiz']


    if bien['Proyecto'] is not None:
        proyecto=[]
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))
        proyecto.append(str(bien['Proyecto']['Id']))


    #PROPIEDAD

    propiedad=[]
    print(str(bien['IdBienRaiz']))
    propiedad.append(str(bien['IdBienRaiz']))
    #propiedad.append(str(bien['Zona']['Id']))
    #propiedad.append(str(bien['EspacioComun']['Id']))
    #try:
        #propiedad.append(str(bien['Proyecto']['Id']))

    #except:
        #propiedad.append(None)

    #Estos son zona, espacio comun y proyecto
    propiedad.append("-1")
    propiedad.append("-1")
    propiedad.append("-1")


    propiedad.append(str(bien['IdTipoPropiedad']))
    propiedad.append(str(bien['IdEstadoPropiedad']))
    propiedad.append(str(bien['IdTipoOperacion']))
    propiedad.append(str(bien['EsUltimaVenta']))
    propiedad.append(str(bien['EsToctoc']))
    propiedad.append(str(bien['PrecioPreponderante']))
    propiedad.append(str(bien['idTipoMonedaPreponderante']))
    propiedad.append(str(bien['Latitud']))
    propiedad.append(str(bien['Longitud']))
    propiedad.append(str(bien['Direccion']))
    propiedad.append(str(bien['DireccionCondominioOEdificio']))
    propiedad.append(str(bien['DireccionCalle']))
    propiedad.append(str(bien['DireccionNumero']))
    propiedad.append(str(bien['DireccionVivienda']))
    propiedad.append(str(bien['ExactitudDireccion']))
    propiedad.append(str(bien['ComunaPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['Comuna']))
    propiedad.append(str(bien['IdComuna']))
    propiedad.append(str(bien['Region']))
    propiedad.append(str(bien['IdRegion']))
    propiedad.append(str(bien['FechaUltimaTransaccion']))
    propiedad.append(str(bien['PrecioValorizacion']))
    propiedad.append(str(bien['PrecioVenta']))
    propiedad.append(str(bien['PrecioArriendo']))
    propiedad.append(str(bien['PrecioArriendoEstimadoPesos']))
    propiedad.append(str(bien['Precio']))
    propiedad.append(str(bien['RolPropiedad']))
    propiedad.append(str(bien['Rol']))
    propiedad.append(str(bien['Subrol']))
    propiedad.append(str(bien['TipoOperacion']))
    propiedad.append(str(bien['Propietario']))
    propiedad.append(str(bien['CantidadDormitorios']))
    propiedad.append(str(bien['CantidadBaños']))
    propiedad.append(str(bien['ImagenStreetView']))
    propiedad.append(str(bien['MetrosTerraza']))
    propiedad.append(str(bien['MetrosTerreno']))
    propiedad.append(str(bien['MetrosConstruccion']))
    propiedad.append(str(bien['IdTipoDestino']))
    propiedad.append(str(bien['TipoDestino']))
    propiedad.append(str(bien['TipoMaterial']))
    propiedad.append(str(bien['Año']))
    propiedad.append(str(bien['AvaluoFiscalTotal']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnterior']))
    propiedad.append(str(bien['AvaluoFiscalExento']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnterior']))
    propiedad.append(str(bien['MorosidadTotal']))
    propiedad.append(str(bien['FechaActualizacionAvaluoFiscal']))
    propiedad.append(str(bien['FechaActualizacionContribucion']))
    propiedad.append(str(bien['AvaluoFiscalTotalPesos']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnteriorPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestralPesos']))
    propiedad.append(str(bien['ContribucionesTrimestralesPesos']))
    propiedad.append(str(bien['ContribucionSemestralAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestral']))
    propiedad.append(str(bien['ContribucionSemestralAnterior']))
    propiedad.append(str(bien['RutaContenido']))
    propiedad.append(str(bien['RutaBienRaiz']))
    propiedad.append(str(bien['OrigenDatoPrecio']))
    propiedad.append(str(bien['CssClassIconoBienRaiz']))
    propiedad.append(str(bien['HistoriaConstruccion']))
    propiedad.append(str(bien['HistoriaContribucion']))
    propiedad.append(str(bien['Titulo']))
    propiedad.append(str(bien['FechaPublicacionDespliegue']))
    propiedad.append(str(bien['IdManzanaReal']))
    propiedad.append(str(bien['ManzanaRealPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['DFL2']))
    propiedad.append(str(bien['FlagEliminado']))
    propiedad.append(str(bien['IdExactitudManzana']))
    propiedad.append(str(bien['IdTipoPropiedadFamilia']))
    propiedad.append(str(bien['IdTipoOperacionFamilia']))




        #propiedad.append(str(bien['Zona']['Id']))
    #propiedad.append(str(bien['EspacioComun']['Id']))
    #try:
        #propiedad.append(str(bien['Proyecto']['Id']))

    #except:
        #propiedad.append(None)

    #Estos son zona, espacio comun y proyecto
    propiedad.append("-1")
    propiedad.append("-1")
    propiedad.append("-1")



    propiedad.append(str(bien['IdTipoPropiedad']))
    propiedad.append(str(bien['IdEstadoPropiedad']))
    propiedad.append(str(bien['IdTipoOperacion']))
    propiedad.append(str(bien['EsUltimaVenta']))
    propiedad.append(str(bien['EsToctoc']))
    propiedad.append(str(bien['PrecioPreponderante']))
    propiedad.append(str(bien['idTipoMonedaPreponderante']))
    propiedad.append(str(bien['Latitud']))
    propiedad.append(str(bien['Longitud']))
    propiedad.append(str(bien['Direccion']))
    propiedad.append(str(bien['DireccionCondominioOEdificio']))
    propiedad.append(str(bien['DireccionCalle']))
    propiedad.append(str(bien['DireccionNumero']))
    propiedad.append(str(bien['DireccionVivienda']))
    propiedad.append(str(bien['ExactitudDireccion']))
    propiedad.append(str(bien['ComunaPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['Comuna']))
    propiedad.append(str(bien['IdComuna']))
    propiedad.append(str(bien['Region']))
    propiedad.append(str(bien['IdRegion']))
    propiedad.append(str(bien['FechaUltimaTransaccion']))
    propiedad.append(str(bien['PrecioValorizacion']))
    propiedad.append(str(bien['PrecioVenta']))
    propiedad.append(str(bien['PrecioArriendo']))
    propiedad.append(str(bien['PrecioArriendoEstimadoPesos']))
    propiedad.append(str(bien['Precio']))
    propiedad.append(str(bien['RolPropiedad']))
    propiedad.append(str(bien['Rol']))
    propiedad.append(str(bien['Subrol']))
    propiedad.append(str(bien['TipoOperacion']))
    propiedad.append(str(bien['Propietario']))
    propiedad.append(str(bien['CantidadDormitorios']))
    propiedad.append(str(bien['CantidadBaños']))
    propiedad.append(str(bien['ImagenStreetView']))
    propiedad.append(str(bien['MetrosTerraza']))
    propiedad.append(str(bien['MetrosTerreno']))
    propiedad.append(str(bien['MetrosConstruccion']))
    propiedad.append(str(bien['IdTipoDestino']))
    propiedad.append(str(bien['TipoDestino']))
    propiedad.append(str(bien['TipoMaterial']))
    propiedad.append(str(bien['Año']))
    propiedad.append(str(bien['AvaluoFiscalTotal']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnterior']))
    propiedad.append(str(bien['AvaluoFiscalExento']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnterior']))
    propiedad.append(str(bien['MorosidadTotal']))
    propiedad.append(str(bien['FechaActualizacionAvaluoFiscal']))
    propiedad.append(str(bien['FechaActualizacionContribucion']))
    propiedad.append(str(bien['AvaluoFiscalTotalPesos']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnteriorPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestralPesos']))
    propiedad.append(str(bien['ContribucionesTrimestralesPesos']))
    propiedad.append(str(bien['ContribucionSemestralAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestral']))
    propiedad.append(str(bien['ContribucionSemestralAnterior']))
    propiedad.append(str(bien['RutaContenido']))
    propiedad.append(str(bien['RutaBienRaiz']))
    propiedad.append(str(bien['OrigenDatoPrecio']))
    propiedad.append(str(bien['CssClassIconoBienRaiz']))
    propiedad.append(str(bien['HistoriaConstruccion']))
    propiedad.append(str(bien['HistoriaContribucion']))
    propiedad.append(str(bien['Titulo']))
    propiedad.append(str(bien['FechaPublicacionDespliegue']))
    propiedad.append(str(bien['IdManzanaReal']))
    propiedad.append(str(bien['ManzanaRealPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['DFL2']))
    propiedad.append(str(bien['FlagEliminado']))
    propiedad.append(str(bien['IdExactitudManzana']))
    propiedad.append(str(bien['IdTipoPropiedadFamilia']))
    propiedad.append(str(bien['IdTipoOperacionFamilia']))

    propiedad2 = []

    for elem in propiedad:
        if not elem is None:
            if elem == "" or elem=='None':
                propiedad2.append(None)
            else:
                propiedad2.append(elem)
        else:
            propiedad2.append(elem)

    insertToctoc.insertar(propiedad2)


    timeDelay = random.randrange(1, 2)
    time.sleep(timeDelay)
