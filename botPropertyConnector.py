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
        sql = "SELECT id2 from portalinmobiliario WHERE link='"+str(link)+"'"
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT id2 from propiedades WHERE link='"+str(link)+"'"
    print(sql)
    cur.execute(sql)
    link = cur.fetchall()
    if len(link)>0:
        return link[0]
    else:
        return link


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
        auxid=obtenerIdConLink(client["link_prop"],client["sitio"])
        if len(auxid)==0:
            return "La propiedad buscada no se encuentra en la base de datos"
        else:
            text = ficha.crearFicha(client["sitio"], auxid, client["mail"], tipoficha)
            return text