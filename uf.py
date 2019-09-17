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
    link='https://valoruf.cl/'
    page3 = requests.get(link)
    tree3 = html.fromstring(page3.content)
    xpath='/html/body/div[2]/h1/span'
    '/html/body/div[2]/h1/span'
    uf=tree3.xpath(xpath)
    try:
        uf=uf[0]
        uf=uf.text
        uf=uf[2:]
        uf=uf.replace(".","")
        uf=uf.replace(",",".")
    except:
        uf=28000.60
    uf=float(uf)
    return(uf)

