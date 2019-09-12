import requests
from bs4 import BeautifulSoup
import random
import pymysql as mysql


def get_proxy():
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,"lxml")
    proxies=[]
    for items in soup.select("tbody tr"):
        proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
        proxies.append(proxy_list)

    proxy = random.choice(proxies)
    proxyDict=\
        {"http": "http://"+str(proxy),
         "https": "http://"+str(proxy),
        }
    return proxyDict

def get_scraped():
    sql = "select IdBienRaiz from propiedadestoctoc"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc2')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    tupla = cur.fetchall()
    mariadb_connection.close()
    scraped = []
    for name in tupla:
        scraped.append(name[0])
    return scraped

def main():
    print(get_scraped())

if __name__ == "__main__":
    main()
