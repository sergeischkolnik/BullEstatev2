from lxml import html
import requests
import agentCreator
import time


def publicacionExiste(link):
    try:
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        tree = html.fromstring(page.content)
    except:
        return False

    paginas = tree.xpath('//*[@id="short-desc"]/div/header/h1')
    if len(paginas)!=0:
        return True
    else:
        return False
    time.sleep(0.3)

def main():
    links = [
        'https://www.portalinmobiliario.com/venta/departamento/estacion-central-metropolitana/5223058-nicasio-retamales-115-uda'
    ]
    for p in links:
        avaible=publicacionExiste(p)
        print(avaible)


if __name__ == '__main__':
    main()
