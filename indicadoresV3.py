import json
import requests


def getUf():
    url = f'https://mindicador.cl/api/'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    # Para que el json se vea ordenado, retornar pretty_json
    pretty_json = json.dumps(data, indent=2)
    return data['uf']['valor']