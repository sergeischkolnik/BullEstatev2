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

    paginas = tree.xpath('//*[@id="wrapper"]/section/div/div[1]/div/h1')
    if len(paginas)!=0:
        if "Esta propiedad ya no" in paginas[0].text:
            return False
        else:
            return True
    else:
        return True
    time.sleep(0.3)

