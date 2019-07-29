import botPropertyDataBase
import botPropertySelect
import botPropertyMain
import botPropertySelect
import ficha
import reportes


def connectorFicha(client):

    text=ficha.crearFicha(client["sitio"],client["id_prop"],client["mail"],1)
    return text