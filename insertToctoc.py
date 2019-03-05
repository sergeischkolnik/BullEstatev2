
import pymysql as mysql

def insertarsql(sql,propiedad):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='toctoc')

    cur = mariadb_connection.cursor()
    cur.execute(sql,propiedad)
    mariadb_connection.commit()
    mariadb_connection.close()
    print("Insertado:" + str(propiedad))
    return



def insertar(propiedad):
    if propiedad[0] is not None:
        sql = """INSERT INTO propiedades(idPropiedad,idZona,idEspacioComun,idProyecto,IdTipoPropiedad,IdEstadoPropiedad,IdTipoOperacion,EsUltimaVenta,EsToctoc,PrecioPreponderante,idTipoMonedaPreponderante,Latitud,Longitud,Direccion,DireccionCondominioOEdificio,DireccionCalle,DireccionNumero,DireccionVivienda,ExactitudDireccion,ComunaPorcentajeDiferenciaAvaluoHabitacional,Comuna,IdComuna,Region,IdRegion,FechaUltimaTransaccion,PrecioValorizacion,PrecioVenta,PrecioArriendo,PrecioArriendoEstimadoPesos,Precio,RolPropiedad,Rol,Subrol,TipoOperacion,Propietario,CantidadDormitorios,CantidadBanos,ImagenStreetView,MetrosTerraza,MetrosTerreno,MetrosConstruccion,IdTipoDestino,TipoDestino,TipoMaterial,Ano,AvaluoFiscalTotal,AvaluoFiscalTotalAnterior,AvaluoFiscalExento,AvaluoFiscalExentoAnterior,MorosidadTotal,FechaActualizacionAvaluoFiscal,FechaActualizacionContribucion,AvaluoFiscalTotalPesos,AvaluoFiscalTotalAnteriorPesos,AvaluoFiscalExentoPesos,AvaluoFiscalExentoAnteriorPesos,ContribucionSemestralPesos,ContribucionesTrimestralesPesos,ContribucionSemestralAnteriorPesos,ContribucionSemestral,ContribucionSemestralAnterior,RutaContenido,RutaBienRaiz,OrigenDatoPrecio,CssClassIconoBienRaiz,HistoriaConstruccion,HistoriaContribucion,Titulo,FechaPublicacionDespliegue,IdManzanaReal,ManzanaRealPorcentajeDiferenciaAvaluoHabitacional,DFL2,FlagEliminado,IdExactitudManzana,IdTipoPropiedadFamilia,IdTipoOperacionFamilia)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
             ON DUPLICATE KEY UPDATE idZona=%s,idEspacioComun=%s,idProyecto=%s,IdTipoPropiedad=%s,IdEstadoPropiedad=%s,IdTipoOperacion=%s,EsUltimaVenta=%s,EsToctoc=%s,PrecioPreponderante=%s,idTipoMonedaPreponderante=%s,Latitud=%s,Longitud=%s,Direccion=%s,DireccionCondominioOEdificio=%s,DireccionCalle=%s,DireccionNumero=%s,DireccionVivienda=%s,ExactitudDireccion=%s,ComunaPorcentajeDiferenciaAvaluoHabitacional=%s,Comuna=%s,IdComuna=%s,Region=%s,IdRegion=%s,FechaUltimaTransaccion=%s,PrecioValorizacion=%s,PrecioVenta=%s,PrecioArriendo=%s,PrecioArriendoEstimadoPesos=%s,Precio=%s,RolPropiedad=%s,Rol=%s,Subrol=%s,TipoOperacion=%s,Propietario=%s,CantidadDormitorios=%s,CantidadBanos=%s,ImagenStreetView=%s,MetrosTerraza=%s,MetrosTerreno=%s,MetrosConstruccion=%s,IdTipoDestino=%s,TipoDestino=%s,TipoMaterial=%s,Ano=%s,AvaluoFiscalTotal=%s,AvaluoFiscalTotalAnterior=%s,AvaluoFiscalExento=%s,AvaluoFiscalExentoAnterior=%s,MorosidadTotal=%s,FechaActualizacionAvaluoFiscal=%s,FechaActualizacionContribucion=%s,AvaluoFiscalTotalPesos=%s,AvaluoFiscalTotalAnteriorPesos=%s,AvaluoFiscalExentoPesos=%s,AvaluoFiscalExentoAnteriorPesos=%s,ContribucionSemestralPesos=%s,ContribucionesTrimestralesPesos=%s,ContribucionSemestralAnteriorPesos=%s,ContribucionSemestral=%s,ContribucionSemestralAnterior=%s,RutaContenido=%s,RutaBienRaiz=%s,OrigenDatoPrecio=%s,CssClassIconoBienRaiz=%s,HistoriaConstruccion=%s,HistoriaContribucion=%s,Titulo=%s,FechaPublicacionDespliegue=%s,IdManzanaReal=%s,ManzanaRealPorcentajeDiferenciaAvaluoHabitacional=%s,DFL2=%s,FlagEliminado=%s,IdExactitudManzana=%s,IdTipoPropiedadFamilia=%s,IdTipoOperacionFamilia=%s"""
        insertarsql(sql,propiedad)
    else:
        a=1
        #insertar idProyecto=1

def insertarLite(propiedad):
    if propiedad[0] is not None:
        sql = """INSERT INTO propiedadesLite(idProp,Lat,Lon,Ano)
             VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Lat=%s,Lon=%s,Ano=%s"""
        insertarsql(sql,propiedad)


