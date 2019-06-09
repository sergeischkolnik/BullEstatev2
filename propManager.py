import pymysql as mysql

def fetchFromTable(db,sql):
	try:
		conn = mysql.connect(user='root', password='sergei', host = '127.0.0.1', database = db)
		cur = conn.cursor()
		cur.execute(sql)
		return cur.fetchall()
	except:
		return -1

def selectorPortal():
	sql = "SELECT COUNT(id) from portalinmobiliario"
	tupla = fetchFromTable("bullestate", sql)
	if tupla != -1:
		num = int(tupla[0][0])
		return num
	else:
		return -1

def selectorGP():
	sql = "SELECT COUNT(id) from goplaceit_scraped"
	tupla = fetchFromTable("goplaceit", sql)
	if tupla != -1:
		num = int(tupla[0][0])
		return num
	else:
		return -1

def getBotClients(hora):
	sql = "select * from clientesBot where activo=1 and horaActualizacion="+str(hora)
	clientes = fetchFromTable("bullestate",sql)
	if clientes != -1:
		return clientes
	else:
		return -1

def getProps(client):
	select = "select link from portalinmobiliario"
	where = " precio>" + str(client[4]) + " and precio<" +str(client[5]) + " and metrosmin>" +str(client[6]) + " and metrosmin<" + str(client[7]) + " and metrosmax>" + str(client[7]) + " and metrosmax<" + str(client[8])

def getLastScrap():
	sql = "select lastscrap from checker where id=1"
	f = fetchFromTable("bullestate",sql)
	if f != -1:
		return f[0][0]
	else:
		return -1

