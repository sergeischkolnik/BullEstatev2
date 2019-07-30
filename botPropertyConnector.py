import botPropertyDataBase
import botPropertySelect
import botPropertyMain
import botPropertySelect
import ficha
import reportes
import pymysql as mysql

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
        if "https" in auxlink:
            print(auxlink)
            auxlink= auxlink.replace('https','http')
        auxlink=auxlink.split('?')
        auxlink=auxlink[0]
        print(auxlink)
        auxid=obtenerIdConLink(auxlink,client["sitio"])
        if len(auxid)==0:
            return "La propiedad buscada no se encuentra en la base de datos"
        else:
            print(auxid[0])
            text = ficha.crearFicha(client["sitio"], auxid[0], client["mail"], tipoficha)
            return text
