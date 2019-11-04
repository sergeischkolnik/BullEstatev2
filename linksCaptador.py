import pymysql as mysql

from sklearn import ensemble
from sklearn.model_selection import train_test_split

from datetime import datetime, timedelta
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)

def main():
    print("obteniendo propiedades")
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql ='select id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,' \
         'estacionamientos,link from duenos inner join portalinmobiliario where ' \
    'duenos.idProp = portalinmobiliario.id2 and ' \
    'duenos.contactado is NULL and ' \
    'duenos.esDueno = "si" and ' \
    'region = "metropolitana" and ' \
    'tipo = "departamento" and ' \
    'fechascrap > "' + str(yesterday) + '"'
    cur.execute(sql)

    resultados = cur.fetchall()
    propsV = [list(x) for x in resultados]
    print("creando modelo")
    clfHV = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                              learning_rate=0.1, loss='huber')

    #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

    preciosV = [row[5] for row in propsV]

    trainingV = []
    for prop in propsV:
        aux = []
        aux.append(int(prop[6]))
        aux.append(int(prop[7]))
        aux.append(int(prop[8]))
        aux.append(int(prop[9]))
        aux.append(prop[10])
        aux.append(prop[11])
        aux.append(int(prop[12]))
        trainingV.append(aux)

    print("Haciendo fit")
    clfHV.fit(trainingV, preciosV)

    print("Recorriendo propiedades")
    for prop in propsV:
        tasacionVenta = int(clfHV.predict([[int(prop[6]),int(prop[7]), int(prop[8]),int(prop[9]), prop[10],prop[11], int(prop[12])]])[0])
        precioReal = int(prop[5])
        delta = precioReal - tasacionVenta
        deltaPorc = (100*delta) / precioReal
        print(str(precioReal) + " vs " + str(tasacionVenta) + " delta%:" + str(deltaPorc))


if __name__ == "__main__":
    main()
