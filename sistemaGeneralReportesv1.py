
import pymysql as mysql

def getClientes():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT * from clientes WHERE activo=1"
    cur.execute(sql)
    clientes = cur.fetchall()
    return clientes

def main():

    clientes = getClientes()
    for cliente in clientes:
        print(cliente)

if __name__ == '__main__':
    main()