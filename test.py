import requests
import agentCreator
from lxml import html
from requests_html import HTMLSession

session = HTMLSession()

newLink="""https://www.portalinmobiliario.com/venta/departamento/las-condes-metropolitana/5053667-el-golf-escuela-militar-inversion-asegurada-uda#position=18&type=item&tracking_id=094e9246-b07c-4a67-a0f0-c4efe0a8f83e"""
r = session.get(newLink)
rtext=r.text
if "profile-info-phone-value" in rtext:
    print("si")
else:
    print("no")