import math
from io import BytesIO

from PIL import Image
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
session = HTMLSession()

url=[]
link='http://www.portalinmobiliario.com/venta/casa/colina-metropolitana/4927298-oportunidad-casa-estilo-chileno-colina-uda?tp=1&op=1&iug=291&ca=2&ts=1&mn=2&or=&sf=1&sp=0&at=0&i=1'
page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
metatext=page.text
metatext=metatext.split(' ')
for meta in metatext:
    if 'https://image.portalinmobiliario.cl/Portal/Propiedades' in meta:
        meta=meta.split('"')
        url.append(meta[1])
        print(meta[1])
url=[]
url.append('https://www.yapo.cl/pg/0EyA2k1K8oD5swNdeCLfpChZEVGMTLxv/0b7HHl9+vQ==.gif')
for x,u in enumerate (url):
    response = requests.get(u)
    img = Image.open(BytesIO(response.content))
    img.save(str(x)+" foto.gif")


comuna=str(link.split('/')[5])
comuna=comuna.replace('-metropolitana','')
comuna=comuna.replace('-',' ')
comuna=comuna.capitalize()
print(comuna)

comuna=str(link.split('/')[6])
comuna=comuna.replace('-metropolitana','')
comuna=comuna.replace('-',' ')
comuna=comuna.capitalize()
print(comuna)

sqlAux1="((portalinmobiliario.dormitorios='1') or (portalinmobiliario.dormitorios='2'))"

sqlDeptosArriendo = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='2019-07-09' and portalinmobiliario.fechapublicacion>'2019-04-15' and " \
          "((portalinmobiliario.link like '%con-con%' and "+sqlAux1+") or " \
          "(portalinmobiliario.link like '%renaca%' and "+sqlAux1+"));"
          # "(portalinmobiliario.link like '%estacion-central%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%macul%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%quinta-normall%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%san-joaquin%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-florida%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%maipu%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-cisterna%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%recoleta%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%renaca%'));"
print(sqlDeptosArriendo)
