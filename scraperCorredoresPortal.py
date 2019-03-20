import datetime
import json
import random
import time
import agentCreator
from itertools import cycle
import requests
from lxml import html
from bs4 import BeautifulSoup
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

proxies=get_proxiestextweb()
proxy_pool = cycle(proxies)

def insertCorredores(mails):
    sql = "SELECT mail from corredores"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    for mail in mails:
        if mail not in lista:
            sql = "INSERT INTO corredores (mail) (" + mail + ")"
            mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
            cur = mariadb_connection.cursor()
            cur.execute(sql)
            mariadb_connection.commit()
            mariadb_connection.close()

def scrapCorredor(link):
    proxi = next(proxy_pool)
    response = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
    soup = BeautifulSoup(response.text, "lxml")
    valores = soup.find_all("td", {"class": "Valor"})
    titulo = soup.find("h1")
    emails = []
    for v in valores:
       if "@" in v:
           emails.append(v)
    insertCorredores(emails)


for id in range(1,219):
    proxi=next(proxy_pool)
    link = "https://www.portalinmobiliario.com/empresas/corredoraspresentes.aspx?p=" + str(id)
    response = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
    soup = BeautifulSoup(response.text, "lxml")
    id = soup.find("table", {"id": "ContentPlaceHolder1_ListViewCorredorasPresentes_groupPlaceholderContainer"})
    links = id.find_all("a")
    linkList = []
    for l in links:
        fullLink = "https://www.portalinmobiliario.com" + str(l.get('href'))
        linkList.append(fullLink)

    for l in linkList:
        scrapCorredor(l)

    timeDelay = random.randrange(0, 1)
    time.sleep(timeDelay)
