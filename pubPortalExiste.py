from lxml import html
import requests
import agentCreator
import time
import reportes
import botPropertyConnector


def publicacionExiste(link):
    try:
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        tree = html.fromstring(page.content)
    except:
        return False

    paginas = tree.xpath('//*[@id="wrapper"]/section/div/div[1]/div/h1')
    if len(paginas)!=0:
        if "Esta propiedad ya no" in paginas[0].text:
            return False
        else:
            return True
    else:
        return True
    time.sleep(0.3)

def main():
    link='http://www.portalinmobiliario.com/venta/departamento/santiago-metropolitana/4925265-av-blanco-encalada-almirante-latorre-uda?tp=2&op=1&iug=441&ca=2&ts=1&mn=1&or=&sf=0&sp=0&at=0&i=86'
    printable=publicacionExiste(link)
    print(printable)
    id=botPropertyConnector.obtenerIdConLink(link,"www.portalinmobiliario.com")
    id=id[0]
    print(id)
    printable=reportes.precio_from_portalinmobiliario(id)
    print(printable)

if __name__ == '__main__':
    main()
