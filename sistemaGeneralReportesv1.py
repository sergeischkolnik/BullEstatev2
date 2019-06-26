
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
        #juntar comunas
        comunas=[]
        if cliente[24] != 'None':
            comunas.append(cliente[24])
        if cliente[25] != 'None':
            comunas.append(cliente[25])
        if cliente[26] != 'None':
            comunas.append(cliente[26])
        if cliente[27] != 'None':
            comunas.append(cliente[27])
        if cliente[28] != 'None':
            comunas.append(cliente[28])
        if cliente[29] != 'None':
            comunas.append(cliente[29])
        print(comunas)

if __name__ == '__main__':
    main()