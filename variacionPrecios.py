import pymysql as mysql
import time
#imports


#funciones
def funcionSql(variable1, variable2, variable3):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT columna1,columna2 FROM nombretabla WHERE condicion"
    cur.execute(sql)
    data = cur.fetchall()
    return data

def obtenerPropiedades(comuna,dormitorios,banos,estacionamientos):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id, fechapublicacion, precio, metrosmin,metrosmax FROM portalinmobiliario WHERE operacion='venta' AND region='metropolitana' AND tipo='departamento' AND dormitorios="+str(dormitorios)+" AND banos="+str(banos)+" and estacionamientos="+str(estacionamientos)+" AND fechapublicacion>='2018-12-16' AND link like '%"+str(comuna)+"%';"
    cur.execute(sql)
    data = cur.fetchall()
    return data


def funcion(variable1,variable2,variable3):
    #funcion
    resultado=variable1+variable2+variable3
    return resultado


def main():
    listaComunas = ["las-condes","santiago","providencia","buin","calera-de-tango","cerrillos","colina","cerro-navia","conchali",
           "curacavi","el-bosque","estacion-central","el-monte","huechuraba","independencia","isla-de-maipo"
           "la-cisterna","la-florida","la-granja","la-pintana","la-reina","lampa","lo-barnechea","lo-espejo",
           "lo-prado","macul","maipu","maria-pinto","melipilla","paine","penalolen","puente-alto","pedro-aguirre-cerda","penaflor",
           "pudahuel","padre-hurtado","pirque","quilicura","quinta-normal","recoleta","renca","san-bernardo","san-miguel","san-ramon",
           "san-joaquin","san-pedro","san-jose-de-maipo","talagante","til-til","vitacura","nunoa"]
    #codigo principal
    #seleccionar desde la base de datos
    #print(listaComunas)
    for comuna in listaComunas:

        #separar departamentos por cantidad de dormitorios, baños y estacionamientos
        for i in range(1,5):
            for j in range (1,5):
                for k in range (0,3):

                    propiedades=obtenerPropiedades(comuna,i,j,k)
                    propiedades=list(propiedades)
                    datos={}

                    for propiedad in propiedades:
                        if propiedad[3]>0 and propiedad[4]>0 and propiedad[2]>0:
                            propiedad=list(propiedad)
                            #sorted(propiedades)
                            #propiedades.sort(key=lambda propiedad:propiedad[0])
                            promedio=(propiedad[3]+propiedad[4])/2
                            preciometro=propiedad[2]/promedio
                            n=(propiedad[1].month)*2
                            if propiedad[1].day<=15:
                                n=n-1
                            #print("mes:")
                            #print(n)
                            if n==24:
                                n=0
                            n=str(n)

                            if n not in datos:
                                datos[n]=[]
                                datos[n].append(preciometro)
                            else:
                                datos[n].append(preciometro)
                            #print(datos[n])
                    avgdatos = {}
                    for w,v in datos.items():
                        v.sort()
                        fiveperc= 0.05*len(v)
                        v=v[(int(fiveperc)):(int(len(v)-fiveperc))]
                        try:
                            avgdatos[w] = sum(v)/ float(len(v))
                        except Exception as error:
                            print(error)
                            avgdatos[w]=0

                    avgdatos["comuna"]=comuna
                    avgdatos["dormitorios"]=i
                    avgdatos["banos"]=j
                    avgdatos["estacionamientos"]=k
                    print(avgdatos)
                    for n in range (0,24):
                        for a,b in avgdatos[w]:
                        difdatos = []
                        difdatos[a,b]= a-b
                        print(str(n)+": "+str(avgdatos[str(n)]))
                        print (difdatos[a,b])



                    #datos.sort(key=lambda datos:datos[0])

                    #se obtiene arreglo de datos ordenados para comuna especifica, dormitorios, baños, estacionamientos especificos

                    # for propiedad[0]:
                    #     SELECT datos from propiedad[0]:
                    #     ORDER BY ()
                    # for d in datos:
                    #     print(d)
                    #
                    #
                    #
                    #
                    #
                    #
                    #     break

                    #calcular el objetivo


        #ordenar los departamentos por comuna
            #SELECT * FROM table_iDjBkE
            #ORDER BY Comuna

        #obtener el promedio de metrosmin y metrosmax de cada departamento
           #for metrosmin and metrosmax:
               #prommetros= (metrosmin + metrosmax)/2
               #print prommetros

        #obtener el promedio de precios por comuna de departamentos de similares características

        #si es que el departamento no tiene estacionamiento, dividir el precio de éste por el promedio de los metros cuadrados, en caso
        #contrario, calcular la diferencia entre el promedio de precios de departamentos con y sin estacionamiento, luego a los departamentos con
        #estacionamiento se le resta esta diferencia de su precio y ya obteniendo esto, se divide por el promedio de metrosmin y metrosmax.
        #if (k=0):
            #print precio/prommetros
        #else:

        #seleccionamos solo los departamentos con fecha de publicación desde el 1 de enero del 2019 y luego por comuna se obtienen el promedio
        #quincenal de precio por metro cuadrado.

        #if fechapublicacion>="2019-01-01"


        #pass
if __name__ == '__main__':
    main()
