import math
from lxml import html
import requests
# import csvWrite as ew
import datetime
import time
from random import randint
from time import sleep
from itertools import cycle
import traceback
from lxml.html import fromstring
from threading import Thread

def getUf():
    try:
        link='https://valoruf.cl/'
        page3 = requests.get(link)
        tree3 = html.fromstring(page3.content)
        xpath='//html/body/div/div/div[2]/div/span[2]'
        '/html/body/div[2]/h1/span'
        uf=tree3.xpath(xpath)
        uf=uf[0]
        uf=uf.text
        uf=uf[2:]
        uf=uf.replace(".","")
        uf=uf.replace(",",".")
    except Exception as e:
        print(e)
        try:
            link='https://www.uf-hoy.com/'
            page3 = requests.get(link)
            tree3 = html.fromstring(page3.content)
            xpath='//*[@id="valor_uf"]/text()'
            uf=tree3.xpath(xpath)
            uf=uf[0]
            uf=uf.replace(".","")
            uf=uf.replace(",",".")
        except Exception as e:
            print(e)
            print("UF NO OBTENIDA")
            uf=28316
    uf=float(uf)
    return(uf)

def main():
    uf1=getUf()
    print(uf1)

if __name__ == '__main__':
    main()
