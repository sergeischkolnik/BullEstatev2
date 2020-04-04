import pymysql as mysql

def obtenedor():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sql = "SELECT id,link from portalinmobiliario limit 100"
    cur.execute(sql)
    list = cur.fetchall()
    return list

def main():
    lista=obtenedor()
    for row in lista:
        link=row[1]
        comuna=link.split("/")[5].replace("-"," ").capitalize()
        print (comuna)

main()