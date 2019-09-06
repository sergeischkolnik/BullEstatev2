import json
import random
import agentCreator
import pymysql as mysql
from itertools import cycle
import time

import requests


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def processDict(D,Master):
    for elem in D.items():
        if elem[1] is not None:
            if elem[0] not in Master:
                if type(elem[1]) is not list and type(elem[1]) is not tuple and type(elem[1]) is not dict:
                    Master[elem[0]] = elem[1]
                if type(elem[1]) is list or type(elem[1]) is dict:
                    process(elem[1],Master)

def process(D,Master):
    if type(D) is dict:
        processDict(D,Master)
    elif type(D) is list:
        D = flatten(D)
        for l in D:
            process(l,Master)

def sacarVariablesBD():
    #sacar lista de variables de la BD

    sql = """select column_name from information_schema.columns where table_name = 'propiedadestoctoc' """

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc2')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    tupla = cur.fetchall()
    mariadb_connection.close()
    listaFinal = []
    for name in tupla:
        listaFinal.append(name[0])
    return listaFinal

def agregarColumna(columnName, tipo):
    sql = "ALTER TABLE propiedadestoctoc ADD COLUMN " + str(columnName) + " " +str(tipo)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc2')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def insertarPropiedad(propDict):
    #En caso de ser remate, inserta en tabla de remates
    sql = "INSERT INTO propiedadestoctoc("
    for k in propDict.keys():
        sql += str(k)+","
    sql = sql[:-1]
    sql += ") VALUES("
    for v in propDict.values():
        sql += "\'" + str(v) + "\',"
    sql = sql[:-1]
    sql += ") ON DUPLICATE KEY UPDATE "
    for i in propDict.items():
        sql += str(i[0]) + "=\'" + str(i[1]) + "\',"
    sql = sql[:-1]

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc2')

    #print(sql)

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    mariadb_connection.commit()
    mariadb_connection.close()
    print("Insertada propiedad:" + str(propDict["IdBienRaiz"]))
    
def main():

    # x = [i for i in range(1000000)]
    # random.shuffle(x)

    for i in range(6000000,7250000):

        masterVar = sacarVariablesBD()
        headers = {
            'sec-fetch-mode': 'cors',
            'cookie': 'X-DATA=98873086-bacb-4c67-9630-f921f2f817dd; _gcl_au=1.1.1050132614.1567703513; _fbp=fb.1.1567703512776.1834989938; _ga=GA1.2.1687249867.1567703522; _gid=GA1.2.1630980933.1567703522; NPS_93546e30_last_seen=1567703521710; __RequestVerificationToken=bBMzbT0DpwlchpCzyFgptd4oA3sdZ3i-IiVhoujkeSgL_P2MEpiCjUSSpkNaxzAiEYh2kAkZ4YmymKzYKtkIkWgt2TjcZ0yty3o7KNb-NvY1; optimizelyEndUserId=oeu1567703541845r0.0295507821834311; optimizelySegments=%7B%222204271535%22%3A%22gc%22%2C%222215970531%22%3A%22false%22%2C%222232940041%22%3A%22direct%22%7D; optimizelyBuckets=%7B%7D; __insp_wid=2107690165; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudG9jdG9jLmNvbS9wcm9waWVkYWRlcy9jb21wcmFudWV2by9kZXBhcnRhbWVudG8vcHJvdmlkZW5jaWEvbW9sbGVyLWVkaWZpY2lvLWx5b24tMjU1MC8xMTE5NDg5P289bGlzdGFkb19jYWx1Z2FfaW1n; __insp_targlpt=RGVwYXJ0YW1lbnRvcyBOdWV2b3MgYSBsYSB2ZW50YSBlbiBQcm92aWRlbmNpYSwgZGUgTW9sbGVyICYgUMOpcmV6LUNvdGFwb3MgUy5BLiwgTW9sbGVyIEVkaWZpY2lvIEx5b24gMjU1MA%3D%3D; __insp_norec_sess=true; __atuvc=9%7C36; __atuvs=5d71478ffef8eeaa008; __insp_slim=1567706242969; X-DATA-NPSW={"CantidadVisitas":1,"FechaCreacion":"2019-09-05T14:11:46.4457584-03:00","FechaUltimoIngreso":"2019-09-05T15:01:55.0949289-03:00","Detalles":[{"TipoVistaNPS":1,"Cantidad":9,"FechaUltimoIngreso":"2019-09-05T14:37:14.2930896-03:00"},{"TipoVistaNPS":2,"Cantidad":3,"FechaUltimoIngreso":"2019-09-05T14:54:05.5199312-03:00"},{"TipoVistaNPS":3,"Cantidad":23,"FechaUltimoIngreso":"2019-09-05T15:01:55.0949289-03:00"}]}; optimizelyPendingLogEvents=%5B%5D; _gat=1; mp_29ae90688062e4e2e6d80b475cef8685_mixpanel=%7B%22distinct_id%22%3A%20%2216d0269ab023a9-0be21a1087fb92-5373e62-15f900-16d0269ab032ad%22%2C%22%24device_id%22%3A%20%2216d0269ab023a9-0be21a1087fb92-5373e62-15f900-16d0269ab032ad%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.toctoc.com%2Fresultados%2Fmapa%2Fcompra%2Fcasa-departamento%2Fmetropolitana%2Fprovidencia%2F%3Fmoneda%3D2%26precioDesde%3D0%26precioHasta%3D0%26dormitoriosDesde%3D%26dormitoriosHasta%3D%26banosDesde%3D0%26banosHasta%3D0%26estado%3D0%26disponibilidadEntrega%3D%26numeroDeDiasTocToc%3D0%26superficieDesdeUtil%3D0%26superficieHastaUtil%3D0%26superficieDesdeConstruida%3D0%26superficieHastaConstruida%3D0%26superficieDesdeTerraza%3D0%26superficieHastaTerraza%3D0%26superficieDesdeTerreno%3D0%26superficieHastaTerreno%3D0%26ordenarPor%3D0%26pagina%3D1%26paginaInterna%3D1%26zoom%3D15%26idZonaHomogenea%3D0%26atributos%3D%26texto%3DProvidencia%2C%2520Santiago%26viewport%3D-33.44984360032895%2C-70.64003981896111%2C-33.40916593228432%2C-70.57843955836275%26idPoligono%3D47%26publicador%3D0%26temporalidad%3D0%22%2C%22%24initial_referring_domain%22%3A%20%22www.toctoc.com%22%7D',
            'x-xsrf-token': 'YNj3aaAeMW0L0TXabCnxaqXi1DYGaDmOPX_V02LSjZhB7LU2zUh-oyTIzVuH1ez2jrVFTyqcb301oOyAbK9zPhybbM8hsZ_LhHdPCeACE0U1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'es-419,es;q=0.9',
            'user-agent': agentCreator.generateAgent(),
            'accept': '*/*',
            'referer': 'https://www.toctoc.com/propiedades/vivienda/a/a/a/' + str(id),
            'authority': 'www.toctoc.com',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin'
        }

        params = (
            ('id', str(i)),
        )

        response = requests.get('https://www.toctoc.com/api/propiedades/bienRaiz/vivienda', headers=headers, params=params)

        json_data = json.loads(response.text)

        try:
            bien = json_data['BienRaiz']
            print("Bien parseado exitosamente")

        except:
            print("error al extraer data")
            continue

        try:
            propiedad_filtrada = dict()
            process(bien,propiedad_filtrada)
        except:
            print("error al crear diccionario")
            continue

        try:
            for b in propiedad_filtrada.items():
                if b[0] not in masterVar:
                    # si la variable no esta en bd
                    tipo = "TEXT"
                    if type(b[1]) is int:
                        tipo = "INT"
                    elif type(b[1]) is float:
                        tipo = "FLOAT"

                    agregarColumna(b[0],tipo)
        except:
            print("error al procesar data")
            continue
        try:
            insertarPropiedad(propiedad_filtrada)
        except:
            print("error al insertar propiedad a la BBDD")
            continue
    
        #time.sleep(20)
                    

if __name__ == "__main__":
    main()
