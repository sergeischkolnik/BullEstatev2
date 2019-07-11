
import pymysql as mysql
import reportes

def getClientes():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT * from clientes WHERE cron=1"
    cur.execute(sql)
    clientes = cur.fetchall()
    return clientes

def main(verboso):

    clientes = getClientes()
    for cliente in clientes:

        #juntar comunas
        comunas=[]
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
        if cliente[30] is not None:
            comunas.append(cliente[30])

        reportes.generarReporteSeparado(preciomin=cliente[5], preciomax=cliente[6], utilmin=cliente[7], utilmax=cliente[8],
                               totalmin=cliente[9], totalmax=cliente[10], latmin=cliente[11], latmax=cliente[12], lonmin=cliente[13],
                               lonmax=cliente[14], dormitoriosmin=cliente[15], dormitoriosmax=cliente[16], banosmin=cliente[17],
                               banosmax=cliente[18], confmin=cliente[40], rentminventa=cliente[36],rentminarriendo=cliente[37],
                               estacionamientos=cliente[19],bodegas=cliente[20], metrodistance=cliente[31],l1=cliente[32],l2=cliente[33],l3=cliente[34],
                               tipo=cliente[21], operacion=cliente[22],
                               region=cliente[24], listaComunas=comunas, prioridad=cliente[39], mail=cliente[3],nombreCliente=cliente[1],
                               idCliente=cliente[0], direccion=cliente[42], radioDireccion=cliente[43],corredor=cliente[41],topx=cliente[44], verboso=verboso)


if __name__ == '__main__':
    main(verboso=True)
