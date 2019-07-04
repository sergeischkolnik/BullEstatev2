
import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudeptoPahola as mailer
import time

past = datetime.now() - timedelta(days=30)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)




sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and ((portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='" + str(yesterday) + "' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.precio<320001 and portalinmobiliario.dormitorios='1') or (portalinmobiliario.precio<450001 and portalinmobiliario.dormitorios='2') or " \
          "(portalinmobiliario.dormitorios>'2' and portalinmobiliario.precio<550001)) and " \
          "(portalinmobiliario.link like '%santiago-metropolitana%' or " \
          "portalinmobiliario.link like '%estacion-central%' or portalinmobiliario.link like '%maipu%' or " \
          "portalinmobiliario.link like '%san-miguel%' or portalinmobiliario.link like '%san-joaquin%' or portalinmobiliario.link like 'macul') or " \
          "(portalinmobiliario.operacion='venta' and portalinmobiliario.tipo='departamento' and portalinmobiliario.fechascrap>='" + str(yesterday) + "' and  " \
          "portalinmobiliario.fechapublicacion>'" + str(past) + "' and portalinmobiliario.link like '%santiago-metropolitana%'));"

print (sql)