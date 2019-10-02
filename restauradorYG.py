import scraperYG as scraper
import pymysql as mysql
from datetime import datetime, timedelta, date
import time
from datetime import datetime, timedelta


def ultimo():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT pagina,region FROM checker WHERE nombrescraper='syg'"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla


while True:
    last=ultimo()
    pagina=last[0][0]
    region = last[0][1]
    try:
        scraper.main(pagina,region,True)
    except:
        print("[SYG] ERROR DE SCRAPER. INICIANDO NUEVAMENTE EN 60 SEGUNDOS")
        time.sleep(60)