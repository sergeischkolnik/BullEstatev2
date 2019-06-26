
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
        if cliente[24] is not None:
            comunas.append(cliente[24])
        if cliente[25] is not None:
            comunas.append(cliente[25])
        if cliente[26] is not None:
            comunas.append(cliente[26])
        if cliente[27] is not None:
            comunas.append(cliente[27])
        if cliente[28] is not None:
            comunas.append(cliente[28])
        if cliente[29] is not None:
            comunas.append(cliente[29])
        dormitoriosMin = int(cliente[15])
        dormitoriosMax = int(cliente[16])
        banosMin = int(cliente[17])
        banosMax = int(cliente[18])
        for comuna in comunas:
            for b in range(banosMin,banosMax+1):
                for d in range(dormitoriosMin,dormitoriosMax+1):
                    print(str(comuna)+","+str(b)+","+str(d))

if __name__ == '__main__':
    main()