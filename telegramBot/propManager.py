import pymysql as mysql

def fetchFromTable(db,sql):
	conn = mysql.connect(user='root', password='sergei', host = '127.0.0.1', database = db)
	cur = conn.cursor()
	cur.execute(sql)
	return cur.fetchall()

def selectorPortal():
	sql = "SELECT COUNT(id) from portalinmobiliario"
	tupla = fetchFromTable("bullestate", sql)
	num = int(tupla[0][0])
	return num

def selectorGP():
	sql = "SELECT COUNT(id) from goplaceit_scraped"
	tupla = fetchFromTable("goplaceit", sql)
	num = int(tupla[0][0])
	return num

def getBotClients(hora):
	sql = "select * from clientesBot where activo=1 and horaActualizacion="+str(hora)
	print(sql)
	clientes = fetchFromTable("bullestate",sql)
	return clientes

def getProps(client):
	select = "select link from portalinmobiliario"
	where = " precio>" + str(client[4]) + " and precio<" +str(client[5]) + " and metrosmin>" +str(client[6]) + " and metrosmin<" + str(client[7]) + " and metrosmax>" + str(client[7]) + " and metrosmax<" + str(client[8])

def getLastScrap():
	sql = "select lastscrap from checker where id=1"
	f = fetchFromTable("bullestate",sql)
	return f[0][0]

