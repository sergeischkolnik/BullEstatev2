import math
from lxml import html
import requests
import datetime
from threading import Thread
import pymysql as mysql
from itertools import cycle
import agentCreator
import time
import random
from requests_html import HTMLSession

link='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&ret=1&cg=1220&o=1'
page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
tree = html.fromstring(page.content)
last=tree.xpath('//*[@id="tabnav"]/li[2]/h2/span[2]')
last=last[0].text
last=last.split(' ')
last=last[5]
last=last.replace('.','')
last=int(last)
last=int(last/50)+1



for i in range(1,last):

    link2='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&ret=1&cg=1220&o='+str(i)
    session = HTMLSession()
    r = session.get(link2)
    links3 = []

    for a in r.html.find('.title'):
        links3.append(a.links.pop())

    for link3 in links3:
        page = requests.get(link3, headers={'User-Agent': agentCreator.generateAgent()})
        tree = html.fromstring(page.content)
        precio1=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/strong')
        precio2=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/span/span')
        if ('UF') in precio2[0].text:
            preciouf=precio2[0].text
            precio=precio1[0].text
        else:
            preciouf=precio1[0].text
            precio=precio2[0].text
        precio=precio.replace('.','')
        precio=precio.replace('$','')
        precio=precio.replace(' ','')
        precio=precio.replace(')','')
        precio=precio.replace('(','')
        precio=precio.replace('*','')
        precio=int(precio)

        preciouf=preciouf.replace('.','')
        preciouf=preciouf.replace('$','')
        preciouf=preciouf.replace(' ','')
        preciouf=preciouf.replace(')','')
        preciouf=preciouf.replace('(','')
        preciouf=preciouf.replace('*','')
        preciouf=preciouf.replace('UF','')
        preciouf=preciouf.replace(',','')
        preciouf=int(preciouf)/100

        codigo=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[21]')
        codigo=int(codigo)
        print("efr")





