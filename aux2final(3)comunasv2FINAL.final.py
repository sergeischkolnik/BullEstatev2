import pymysql as mysql

def obtenedor():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id,link from portalinmobiliario"
    cur.execute(sql)
    list = cur.fetchall()
    return list
def sanitizar(sucio):
    limpio = sucio.replace("-arica-y-parinacota","")
    limpio = limpio.replace("-tarapaca", "")
    limpio = limpio.replace("-antofagasta", "")
    limpio = limpio.replace("-atacama", "")
    limpio = limpio.replace("-coquimbo", "")
    limpio = limpio.replace("-valparaiso", "")
    limpio = limpio.replace("-metropolitana", "")
    limpio = limpio.replace("-bernardo-ohiggins", "")
    limpio = limpio.replace("-maule", "")
    limpio = limpio.replace("-nuble", "")
    limpio = limpio.replace("-biobio", "")
    limpio = limpio.replace("-la-araucania", "")
    limpio = limpio.replace("-de-los-rios", "")
    limpio = limpio.replace("-los-lagos", "")
    limpio = limpio.replace("-aysen", "")
    limpio = limpio.replace("-magallanes-y-antartica-chilena", "")
    return limpio


def main():
    lista=obtenedor()
    for x,row in enumerate(lista):
        try:
            link=row[1]
            id = row[0]
            if "/MLC-/" in link:
                comuna=""
                print("N°: " + str(x) + " - ID: " + str(id) + ", Comuna: " + comuna)
                continue
            n=5
            if ("/do/" in link or "/do-de-temporada/" in link):
                n=6
            comuna=(sanitizar(link.split("/")[n])).replace("-"," ")
            if (comuna=="departamento" or comuna=="casa"):
                print("N°: " + str(x) + " - ID: " + str(id) + ", Comuna: " + comuna)
                print(link)
                break
            print("N°: " + str(x) + " - ID: " + str(id) + ", Comuna: " + comuna)
        except:
            comuna=""
            print("N°: " + str(x) + " - ID: " + str(id) + ", Comuna: " + comuna)
main()