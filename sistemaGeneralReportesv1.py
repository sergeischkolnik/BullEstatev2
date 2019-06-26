
import pymysql as mysql
import reportes.py

def getClientes():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT * from clientes WHERE activo=1"
    cur.execute(sql)
    clientes = cur.fetchall()
    return clientes

def main(verboso):

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

        reportes.generarReporteSeparado(preciomin=cliente[5], preciomax=cliente[6], utilmin=cliente[7], utilmax=cliente[8],
                               totalmin=cliente[9], totalmax=cliente[10], latmin=cliente[11], latmax=cliente[12], lonmin=cliente[13],
                               lonmax=cliente[14], dormitoriosmin=cliente[15], dormitoriosmax=cliente[16], banosmin=cliente[17],
                               banosmax=cliente[18], confmin=cliente[39], rentminventa=cliente[35],rentminarriendo=cliente[36],
                               estacionamientos=cliente[19], metrodistance=cliente[30], tipo=cliente[20], operacion=cliente[21],
                               region=cliente[23], listaComunas=comunas, prioridad=cliente[38], mail=cliente[3],
                               nombreCliente=cliente[1], direccion=cliente[41], radioDireccion=cliente[42], verboso=verboso)


if __name__ == '__main__':
    main(verboso=True)