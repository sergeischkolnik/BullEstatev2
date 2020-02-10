import selenium
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os
import time
import random
from lxml import html
import requests

def target(region,operacion,tipo):
    if operacion=='venta':
        op='1220'
    else:
        op='1240'

    link=''
    return link


def updateArchivoContactados(lista):
    f=open("contactadosYapo.txt", "w")
    for e in lista:
        f.write(str(e)+"\n")
    f.close()

def cargarContactados():
    f=open("contactadosYapo.txt", "r")
    contents = f.read()
    list = contents.split("\n")
    f.close()
    return list[:-1]

def initialize():
    #Cargar pagina inicial
    #driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe',chrome_options=chrome_options)
    driver.get('https://www.yapo.cl')
    #driver.get('https://www.mercadolibre.com/jms/mlc/lgz/msl/login/H4sIAAAAAAAEAyWNQQ6DMAwE_-IzgnuO_UjkBgNWHRwlRmmF-HtNe9zx7vgE0ZX3aJ9CEIDeRTixwQBF0BatOfLsh8KOGhv9Y5Z0V7BiJqPaIJy3aKX5QT66VQtKIy_hYVtcRLuz3y9nq3rYzEoL09R7H4tWQ-E965OFsbKOSfME1-CeZtEqphcEqwddX9nqXW2zAAAA/user')
    driver.maximize_window()

    print("Quedan 3 s")
    time.sleep(3)
    return driver


def login(driver):
    #Ingresar con contraseña y Clave
    mail_box=driver.find_element_by_id('user_id')
    enter_button=driver.find_element_by_class_name('andes-button__content')
    mail='contacto@vendetudepto.cl'
    for c in mail:
        mail_box.send_keys(c)
        time.sleep(0.5)
        time.sleep(random.randint(0,1))
    enter_button.click()
    time.sleep(random.randint(5,15))
    pswd_box=driver.find_element_by_id('password')
    pswd_box.send_keys('Bullestate.123')
    login_btn=driver.find_element_by_id('action-complete')
    login_btn.click()
    time.sleep(random.randint(5,15))

def contactPublication(driver,link,text,inicialLink):
    print("tratando de contactar a: "+str(link))
    name=['Carolina Guevara','Daniela Rodriguez','Pablo Galleguillos','Xaviera Kuhlmann']
    mail=['carolina@vendetudepto.cl','daniela@vendetudepto.cl','pablo@vendetudepto.cl','xaviera@vendetudepto.cl']
    telefono=['+56936838747','+56977560015','+56990898881','+56984794086']
    if "metropolitana" in inicialLink:
        rand=random.randint(0,1)
        tagregion="Metropolitana"
    elif "valparaiso" in inicialLink:
        rand=random.randint(2,3)
        tagregion="Valparaiso"
    else:
        return
    if rand==1:
        text=text.replace('Carolina','Daniela')
        text=text.replace('Guevara','Rodriguez')
        text=text.replace('carolina','daniela')
        text=text.replace('+569 3683 8747','+569 7756 0015')
    if rand==2:
        text=text.replace('Carolina','Pablo')
        text=text.replace('Guevara','Galleguillos')
        text=text.replace('carolina','pablo')
        text=text.replace('+569 3683 8747','+569 9089 8881')
    if rand==3:
        text=text.replace('Carolina','Xaviera')
        text=text.replace('Guevara','Kuhlmann')
        text=text.replace('carolina','xaviera')
        text=text.replace('+569 3683 8747','+569 8479 4086')

    #cambiar a publicación
    time.sleep(random.randint(25,45))
    driver.get(link)
    time.sleep(random.randint(5,15))
    #enviar mensaje
    text_box_name = driver.find_element_by_id('your_name')

    text_box_email = driver.find_element_by_id('user_email')
    text_box_phone = driver.find_element_by_id('phone')
    text_box_message = driver.find_element_by_id('adreply_body')
    send_button = driver.find_element_by_id('send')
    text_box_name.send_keys(name[rand])
    text_box_email.send_keys(mail[rand])
    text_box_phone.send_keys(telefono[rand])
    text_box_message.send_keys(text)
    time.sleep(random.randint(5,15))
    print(str(link)+ " contactado ("+str(tagregion)+")")
    send_button.click()

def main(linkedTextList,inicialLink):
    driver = initialize()
    #login(driver)
    for linkedText in linkedTextList:
        try:
            contactPublication(driver,linkedText[0],linkedText[1],inicialLink)
        except Exception as E:
            print(E)
        time.sleep(random.randint(5,15))


if __name__ == "__main__":

    headers1 = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; PI=d50qlpmdqz1qdv4lynbllh0w; __RequestVerificationToken=NK9YOkOtc3k6bUsfzF0OyZa_kYCBJlPtdTSyYK97lihubPSwAGhZp8pigJ1j5S6LOPG3PlvaiaCMpSoomr7Ez00OFHw1; uniqueID=4df06d9b-bd2e-4565-bff5-9d30c15ea7b2; _ga=GA1.1.434386957.1551705638; _hjid=f5243996-1bed-4c3a-9d9b-0468976dd33e; Buscador=Region=356&IDBusquedaUnidadGeopolitica=356&TipoPropiedad=Departamento; AWSELB=7517F7ED0C3C5C3E0C8743D6A3E725F2C6421325348258AB2B2B6C24C55B97E7B421F62FEDE1E3B33663FE99C845602640543858273DAF905910FD5E38A1B2D3F9329B42B1; _mlt=d8ec613f-94d1-479b-9224-07a09b8ecc69; pin_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; _pi_ga=GA1.2.901507403.1570560325; _pi_ci=901507403.1570560325; _d2id=10753c94-136c-426d-b536-52f4bdc9ad06; _csrf=wiPGYePC-rZQJpMMJMEqYZv_; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiJwcm92aWRlbmNpYSIsInNlbGVjdGVkIjoiIn0sImZpbHRlci1uZXciOnsiY2hlY2tlZCI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZX19; JSESSIONID=4EE983A7EB482E20624672E4E17AF4E8; pmsctx=******IMLC507223027%7C%7CIMLC507775718%7CIMLC508093497%7C%7C**; navigation_items=MLC507223027%7C14102019125752-MLC507775718%7C14102019125042-MLC508093497%7C08102019190408-MLC507769027%7C08102019184813-MLC507748684%7C08102019184550; c_home=0.0.6-redirect-circular-ref%7C5.2.0; pin_exp=new; _pi_ga_gid=GA1.2.1582383825.1571164864',
}

    inicialLinkVentaSantiago='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&cmn=305&cmn=307&cmn=313&cmn=315&cmn=316&cmn=323&cmn=330&cmn=335&cmn=340&cmn=343&cmn=346&ret=1&cg=1220&f=p&o='
    inicialLinkArriendoSantiago='https://www.yapo.cl/region_metropolitana/arrendar?ca=15_s&cmn=305&cmn=307&cmn=313&cmn=315&cmn=316&cmn=323&cmn=330&cmn=335&cmn=340&cmn=343&cmn=346&ret=1&cg=1240&f=p&o='
    inicialLinkVentaDeptoValpo='https://www.yapo.cl/valparaiso/comprar?ca=6_s&cmn=52&cmn=79&cmn=81&ret=1&cg=1220&f=p&o='
    inicialLinkArriendoDeptoValpo='https://www.yapo.cl/valparaiso/comprar?ca=6_s&cmn=52&cmn=79&cmn=81&ret=1&cg=1240&f=p&o='

    inicials=[]
    inicials.append(inicialLinkVentaSantiago)
    inicials.append(inicialLinkArriendoSantiago)
    inicials.append(inicialLinkVentaDeptoValpo)
    inicials.append(inicialLinkArriendoDeptoValpo)



    body1 = "Hola!\n\n"
    body1 += "Mi nombre es Carolina, trabajo en Vendetudepto.cl. Hoy te tengo excelentes noticias!!.\n\n"
    body1 += "Hemos seleccionado tu propiedad, para ser parte de nuestro programa de fidelización. Tenemos ofertas de hasta 100% de descuento en nuestras comisiones  \n\n"
    body1 += "Nuestro servicio incluye publicaciones con cuentas pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión de visitas.\n"
    body1 += "Además, realizamos el acompañamiento hasta la firma final de compraventa o de arriendo de la propiedad.\n\n"
    body1 += "Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo carolina@vendetudepto.cl, junto a tu número de contacto.\n\n"
    body1 += "Ante cualquier duda, por favor escríbeme al correo o a mi WhatsApp +569 3683 8747.\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Carolina Guevara, \n"
    body1 += "www.vendetudepto.cl"

    body2="""Hola! Soy Carolina, agente de www.vendetudepto.cl y hoy te tengo excelentes noticias!

        Nuestra empresa es una plataforma de inversión inmobiliaria que detecta oportunidades de mercado mediante algoritmos de inteligencia artificial, y hemos seleccionado tu propiedad para ser parte de nuestro programa de fidelización con tarifas preferenciales de nuestros honorarios. 
        
        Para colaborar con tu gestión comercial, nuestro servicio se compone por: 
        -Tasación con nuestro modelo.
        -Sesión fotográfica.
        -Difusión con nuestra cartera de inversionistas, cuentas pagadas en los principales portales de compraventa inmboliaria y redes sociales.
        -Gestión de visitas.
        -Asesoría integral durante todo el proceso.
        
        Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo carolina@vendetudepto.cl, junto a tu número de contacto. 
        Ante cualquier duda, por favor escríbeme al correo o a mi WhatsApp +569 3683 8747. 
        
        Quedo a tu disposición! 
        Atentamente.
        Carolina Guevara
        www.vendetudepto.cl
        
        Manquehue Norte 151 of. 703, Las Condes"""

    for inicialLink in inicials:
        for i in range (1,200):
            testList = []
            contactados = cargarContactados()
            contactados = list(dict.fromkeys(contactados))

            inicialLink+=str(i)

            print(inicialLink)
            page=requests.get(inicialLink, headers=headers1)
            idlist=[]
            tree=html.fromstring(page.content)
            sublink=tree.xpath('//*[@id="69702573"]/td[3]/a[1]')

            page=page.text.split('" class="ad listing_thumbs')
            for p in page:
                p=p[-8:]
                try:
                    p=int(p)
                    idlist.append(p)
                except:
                    pass
            print("se han encontrado "+str(len(idlist))+" links.")
            if len(idlist)>0:
                for id in idlist:
                    if id in contactados:
                        pass
                    else:
                        contactados.append(id)
                        link='https://www.yapo.cl/region_metropolitana/_'+str(id)+'.htm?ca=15'
                        body=body2+'\nRef: '+str(id)
                        p1=[link,body]
                        testList.append(p1)
                updateArchivoContactados(contactados)
                main(testList,inicialLink)
            else:
                print("Fin Captación")
                break


