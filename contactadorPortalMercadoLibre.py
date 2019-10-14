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
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    driver.get('https://www.mercadolibre.com/jms/mlc/lgz/msl/login/H4sIAAAAAAAEAyWNQQ6DMAwE_-IzgnuO_UjkBgNWHRwlRmmF-HtNe9zx7vgE0ZX3aJ9CEIDeRTixwQBF0BatOfLsh8KOGhv9Y5Z0V7BiJqPaIJy3aKX5QT66VQtKIy_hYVtcRLuz3y9nq3rYzEoL09R7H4tWQ-E965OFsbKOSfME1-CeZtEqphcEqwddX9nqXW2zAAAA/user')
    driver.maximize_window()
    time.sleep(random.randint(5,15))
    return driver

def login(driver):
    #Ingresar con contraseña y Clave
    mail_box=driver.find_element_by_id('user_id')
    enter_button=driver.find_element_by_class_name('ui-button')
    mail_box.send_keys('contacto@vendetudepto.cl')
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
    print("Enviado para:" + str(link))
    send_button.click()

def main(linkedTextList):
    driver = initialize()
    login(driver)
    for linkedText in linkedTextList:
        contactPublication(driver,linkedText[0],linkedText[1])
        time.sleep(random.randint(10,20))


if __name__ == "__main__":
    testList = []
    p1 = ["https://www.portalinmobiliario.com/venta/departamento/vina-del-mar-valparaiso/5130321-miraflores-espectacular-vista-uda",
          "Hola! Prueba miraflores"]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/venta/departamento/vina-del-mar-valparaiso/5113141-recreo-4d4b-vista-y-terminaciones-de-lujo-uda",
          "prueba valpo "]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/arriendo/casa/vina-del-mar-valparaiso/5111542-renaca-tranquilo-sector-rodeado-de-naturaleza-uda,"
          "prueba reñaca"]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/arriendo/departamento/quilpue-valparaiso/5101326-departamento-3d2b-nuevo-calle-condell-sur-uda",
          "prueba condel"]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana/5095654-san-damian-081-uda",
          "prueba san damian"]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/venta/casa/colina-metropolitana/5095584-guay-guay-10701-uda",
          "prueba para casa colina"]
    testList.append(p1)
    p1 = ["https://www.portalinmobiliario.com/venta/departamento/la-cisterna-metropolitana/5116216-goycolea-salas-uda",
          "prueba para la cisterna"]
    testList.append(p1)
    main(testList)

