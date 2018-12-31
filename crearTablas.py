import psycopg2


conn = psycopg2.connect(database="bullestate", user="supersergei", password="sergei", port=5432)


cur = conn.cursor()

for tipo in ["departamento","casa"]:
    for d in range(1,5):
        for b in range(1,d+1):
            for op in ["venta_venta", "venta_arriendo", "arriendo_arriendo"]:
                for lugar in ["metropolitana", "regiones"]:
                    name = "d_" + str(tipo) + "_" + str(d) + "_" + str(b) + "_" + op + "_" + lugar
                    sqlSeq = "CREATE SEQUENCE \"public\"." + name + "_seq START WITH 1;"
                    sqlTable = "CREATE TABLE \"public\".\"" + name + "\" ( \"id\" integer DEFAULT nextval(\'\"" + name + "_seq\"\'::regclass),\"prop1\" integer, \"prop2\" integer, \"distancia\" numeric, PRIMARY KEY (\"id\"), FOREIGN KEY (\"prop1\") REFERENCES \"public\".\"propiedades\"(\"id\"), FOREIGN KEY (\"prop2\") REFERENCES \"public\".\"propiedades\"(\"id\"));"
                    try:
                        cur.execute(sqlTable)
                    except:
                        print("")
                    try:
                        conn.commit()
                    except:
                        print("")





conn.close()