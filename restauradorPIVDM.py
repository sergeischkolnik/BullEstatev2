import scraperportalinmobiliariovRM as scraper
import pymysql as mysql
from datetime import datetime, timedelta, date
import time
from datetime import datetime, timedelta


def ultimo():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT operacion,tipo,region,pagina FROM checker WHERE nombrescraper='spivm'"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla

saltopagina=0
while True:
    last=ultimo()[0]
    tipo=last[1]
    op=last[0]
    region=last[2]
    pagina=last[3]
    pagina+=saltopagina
    saltopagina=0
    try:
        scraper.Main(tipo,op,region,pagina,True)
    except:
        print("[SPIVM] ERROR DE SCRAPER. INICIANDO NUEVAMENTE EN 60 SEGUNDOS")
        time.sleep(60)
        saltopagina=1
