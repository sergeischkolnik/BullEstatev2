from lxml import html
import requests
import agentCreator
import time


def publicacionExiste(link):
    try:
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        if "El link al que estás intentando acceder no corresponde a ninguna página de nuestro sitio" in page.text:
            return False
        else:
            return True

    except:
        return False

    time.sleep(0.3)

def main():
    links = [
        'https://www.yapo.cl/metropolitana/69770567','https://www.yapo.cl/region_metropolitana/69770567','https://www.yapetropolitana/69770567'
    ]
    for p in links:
        avaible=publicacionExiste(p)
        print(avaible)


if __name__ == '__main__':
    main()
