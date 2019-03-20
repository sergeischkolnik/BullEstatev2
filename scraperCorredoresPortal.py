import datetime
import json
import random
import time
import agentCreator
from itertools import cycle
import requests
from lxml import html
from bs4 import BeautifulSoup

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

def scrapCorredor(link):
    proxi = next(proxy_pool)
    response = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
    soup = BeautifulSoup(response.text, "lxml")
    valores = soup.find_all("td", {"class": "Valor"})
    titulo = soup.find("h1")
    print(titulo.string)
    for v in valores:
        print(v.string)



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

    timeDelay = random.randrange(1, 2)
    time.sleep(timeDelay)
