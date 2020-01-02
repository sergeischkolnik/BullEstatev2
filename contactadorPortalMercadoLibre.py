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

def initialize():
    #Cargar pagina inicial
    #driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe',chrome_options=chrome_options)
    driver.get('https://www.mercadolibre.com/jms/mlc/lgz/msl/login/')
    #driver.get('https://www.mercadolibre.com/jms/mlc/lgz/msl/login/H4sIAAAAAAAEAyWNQQ6DMAwE_-IzgnuO_UjkBgNWHRwlRmmF-HtNe9zx7vgE0ZX3aJ9CEIDeRTixwQBF0BatOfLsh8KOGhv9Y5Z0V7BiJqPaIJy3aKX5QT66VQtKIy_hYVtcRLuz3y9nq3rYzEoL09R7H4tWQ-E965OFsbKOSfME1-CeZtEqphcEqwddX9nqXW2zAAAA/user')
    driver.maximize_window()
    print("Quedan 60 s")
    time.sleep(15)
    print("Quedan 45 s")
    time.sleep(15)
    print("Quedan 30 s")
    time.sleep(15)
    print("Quedan 15 s")
    time.sleep(15)
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

def contactPublication(driver,link,text):
    #cambiar a publicación
    time.sleep(random.randint(5,15))
    driver.get(link)
    time.sleep(random.randint(5,15))
    #enviar mensaje
    text_box = driver.find_element_by_id('question')
    send_button = driver.find_element_by_id('question-btn')
    text_box.clear()
    text_box.send_keys(text)
    time.sleep(random.randint(5,15))
    print(str(link)+ " contactado")
    send_button.click()

def main(linkedTextList):
    driver = initialize()
    #login(driver)
    for linkedText in linkedTextList:
        contactPublication(driver,linkedText[0],linkedText[1])
        time.sleep(random.randint(10,20))


if __name__ == "__main__":
    testList = []

    body1 = "Hola!\n\n"
    body1 += "Te escribo por tu publicación en Portalinmobiliario \n\n"


    body1 += "Mi nombre es Carolina, trabajo en Vendetudepto.cl, y como promoción de lanzamiento, estamos ofreciendo servicios Totalmente Gratuitos de difusión inmobiliaria.\n\n"
    body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad (y si lo deseas, puedes seguir gestionándolo por tu lado).\n\n"

    body1 += "El servicio incluye publicaciones con cuentas pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión de visitas. Como te mencioné anteriormente, esto no tiene absolutamente ningún costo para ti.\n"
    body1 += "Además, realizamos el acompañamiento hasta la firma final de compraventa o de arriendo de la propiedad.\n\n"
    body1 += "Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo carolina@vendetudepto.cl (precio, características, horarios de visita, fotografías, etc), y con gusto asignaremos un corredor para tu propiedad. Junto con esto, rogamos enviarnos tu número de contacto.\n\n"
    body1 += "Ante cualquier dudas, por favor escríbeme al correo o a nuestro WhatsApp +569 8936 6288.\n"
    body1 += "De antemano muchas gracias por tu tiempo,\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Carolina, \n"
    body1 += "www.vendetudepto.cl\n\n"
    body1 += "PD: Si usted es corredor de propiedades, rogamos indicar si la propiedad está disponible para canje."

    p1 = ["https://www.portalinmobiliario.com/venta/casa/vina-del-mar-valparaiso/5205917-solida-casa-5d3b-recreo-uda",
          body1]
    testList.append(p1)

    main(testList)

