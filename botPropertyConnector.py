import botPropertyDataBase
import botPropertySelect
import botPropertyMain
import botPropertySelect
import ficha
import reportes

def obtenerIdConLink(link,sitio):

    if (sitio=='portal'):
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        sql = "SELECT id2 from portalinmobiliario WHERE link="+str(link)
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT id2 from propiedades WHERE link="+str(link)
    cur.execute(sql)
    link = cur.fetchall()
    if len(link)>0:
        return link[0]
    else:
        return link


def connectorFicha(client):

    if not cliente["fichapro"] and not cliente["fichainterna"]:
        tipoficha=1
    elif cliente["fichapro"] and not cliente["fichainterna"]:
        tipoficha=2
    elif not cliente["fichapro"] and cliente["fichainterna"]:
        tipoficha=3
    else:
        tipoficha=4

    if "id_prop" in client:
        text=ficha.crearFicha(client["sitio"],client["id_prop"],client["mail"],tipoficha)
    else:
        auxid=obtenerIdConLink(client["link_prop"],client["sitio"])
        text = ficha.crearFicha(client["sitio"], auxid, client["mail"], tipoficha)
    return text