import pymysql as mysql

def insertarsql(sql,nombreTabla,nombreId):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc')

    cur = mariadb_connection.cursor()
    sql = "INSERT INTO " + nombreTabla + sql
    cur.execute(sql)

    id=cur.lastrowid


    mariadb_connection.commit()
    mariadb_connection.close()
    if id == 0:
        return id


#sql = "(idPropiedad,idZona,idEspacioComun,idProyecto,IdTipoPropiedad) VALUES(66,1,1,1,88) ON DUPLICATE KEY UPDATE IdTipoPropiedad=77"


#print(insertarsql(sql,nombreTabla="propiedades"))
text= """ propiedad.append(str(bien['IdBienRaiz']))
    propiedad.append(str(bien['Zona']['Id']))
    propiedad.append(str(bien['EspacioComun']['Id']))
    propiedad.append(str(bien['Proyecto']['Id']))
    propiedad.append(str(bien['IdTipoPropiedad']))
    propiedad.append(str(bien['IdEstadoPropiedad']))
    propiedad.append(str(bien['IdTipoOperacion']))
    propiedad.append(str(bien['EsUltimaVenta']))
    propiedad.append(str(bien['EsToctoc']))
    propiedad.append(str(bien['PrecioPreponderante']))
    propiedad.append(str(bien['idTipoMonedaPreponderante']))
    propiedad.append(str(bien['Latitud']))
    propiedad.append(str(bien['Longitud']))
    propiedad.append(str(bien['Direccion']))
    propiedad.append(str(bien['DireccionCondominioOEdificio']))
    propiedad.append(str(bien['DireccionCalle']))
    propiedad.append(str(bien['DireccionNumero']))
    propiedad.append(str(bien['DireccionVivienda']))
    propiedad.append(str(bien['ExactitudDireccion']))
    propiedad.append(str(bien['ComunaPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['Comuna']))
    propiedad.append(str(bien['IdComuna']))
    propiedad.append(str(bien['Region']))
    propiedad.append(str(bien['IdRegion']))
    propiedad.append(str(bien['FechaUltimaTransaccion']))
    propiedad.append(str(bien['PrecioValorizacion']))
    propiedad.append(str(bien['PrecioVenta']))
    propiedad.append(str(bien['PrecioArriendo']))
    propiedad.append(str(bien['PrecioArriendoEstimadoPesos']))
    propiedad.append(str(bien['Precio']))
    propiedad.append(str(bien['RolPropiedad']))
    propiedad.append(str(bien['Rol']))
    propiedad.append(str(bien['Subrol']))
    propiedad.append(str(bien['TipoOperacion']))
    propiedad.append(str(bien['Propietario']))
    propiedad.append(str(bien['CantidadDormitorios']))
    propiedad.append(str(bien['CantidadBaños']))
    propiedad.append(str(bien['ImagenStreetView']))
    propiedad.append(str(bien['MetrosTerraza']))
    propiedad.append(str(bien['MetrosTerreno']))
    propiedad.append(str(bien['MetrosConstruccion']))
    propiedad.append(str(bien['IdTipoDestino']))
    propiedad.append(str(bien['TipoDestino']))
    propiedad.append(str(bien['TipoMaterial']))
    propiedad.append(str(bien['Año']))
    propiedad.append(str(bien['AvaluoFiscalTotal']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnterior']))
    propiedad.append(str(bien['AvaluoFiscalExento']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnterior']))
    propiedad.append(str(bien['MorosidadTotal']))
    propiedad.append(str(bien['FechaActualizacionAvaluoFiscal']))
    propiedad.append(str(bien['FechaActualizacionContribucion']))
    propiedad.append(str(bien['AvaluoFiscalTotalPesos']))
    propiedad.append(str(bien['AvaluoFiscalTotalAnteriorPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoPesos']))
    propiedad.append(str(bien['AvaluoFiscalExentoAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestralPesos']))
    propiedad.append(str(bien['ContribucionesTrimestralesPesos']))
    propiedad.append(str(bien['ContribucionSemestralAnteriorPesos']))
    propiedad.append(str(bien['ContribucionSemestral']))
    propiedad.append(str(bien['ContribucionSemestralAnterior']))
    propiedad.append(str(bien['RutaContenido']))
    propiedad.append(str(bien['RutaBienRaiz']))
    propiedad.append(str(bien['OrigenDatoPrecio']))
    propiedad.append(str(bien['CssClassIconoBienRaiz']))
    propiedad.append(str(bien['HistoriaConstruccion']))
    propiedad.append(str(bien['HistoriaContribucion']))
    propiedad.append(str(bien['Proyecto']))
    propiedad.append(str(bien['Titulo']))
    propiedad.append(str(bien['FechaPublicacionDespliegue']))
    propiedad.append(str(bien['IdManzanaReal']))
    propiedad.append(str(bien['ManzanaRealPorcentajeDiferenciaAvaluoHabitacional']))
    propiedad.append(str(bien['DFL2']))
    propiedad.append(str(bien['FlagEliminado']))
    propiedad.append(str(bien['IdExactitudManzana']))
    propiedad.append(str(bien['IdTipoPropiedadFamilia']))
    propiedad.append(str(bien['IdTipoOperacionFamilia'])))"""
text2=""
text=text.split('\n')
for t in text:
    t=t.split("'")
    text2=text2+str(t[1])+"=%s,"
print (text2)
