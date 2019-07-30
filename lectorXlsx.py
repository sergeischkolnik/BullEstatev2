import xlrd
import pymysql as mysql

loc = ("CodigoUnicoTerritorialRegionesyComunas_1391672726892072087.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

def insert(client):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sqlInsertInto = "INSERT INTO comunas (idregion,region,idprovincia,provincia,idcomuna,comuna)"
    sqlValues = "VALUES ('"+str(client[0])+"','"+str(client[1])+"','"+str(client[2])+"','"+str(client[3])+"','"+str(client[4])+"','"+str(client[5])+"')"
    sql=sqlInsertInto+" "+sqlValues
    print(sql)
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()


data=[]
for j in range(sheet.nrows):
    row=[]
    for i in range(sheet.ncols):
        row.append(sheet.cell_value(j, i))
        insert(row)
    data.append(row)

print(data)

