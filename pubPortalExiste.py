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
    if "finalizada" in page.text:
        return False
    elif len(paginas)!=0:
        return True
    else:
        return False
    time.sleep(0.3)

def main():
    links = [
        'https://www.portalinmobiliario.com/venta/departamento/las-condes-metropolitana/5188804-escuela-militar-amoblado-uda#reco_item_pos=0&reco_backend=triggered_portalinmobiliario_recommendations&reco_backend_type=function&reco_client=classi-portalinmobiliario-vip&reco_id=83e6dea1-e850-454f-821d-23d890ecfbc3'
    ]
    for p in links:
        avaible=publicacionExiste(p)
        print(avaible)


if __name__ == '__main__':
    main()
