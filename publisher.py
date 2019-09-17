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

prop={}
prop["tipo"]="Departamento"
prop["dorms"]="2"
prop["baths"]="2"
prop["util"]="60"
prop["total"]="65"
prop["comuna"]="Santiago"
prop["descrpicion"]="Hermoso Depto"





dBase_xpath = "//h4[text()='Searchable Database']"

#Cargar pagina inicial
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads\chromedriver.exe')
driver.get('https://seguidor.portalinmobiliario.cl/vendetudepto')
driver.maximize_window()

#Ingresar con contraseña y Clave
mail_box=driver.find_element_by_id('txtEmail')
pass_box=driver.find_element_by_id('txtPassword')
enter_button=driver.find_element_by_id('btnIngresar')
mail_box.send_keys('contacto@vendetudepto.cl')
pass_box.send_keys('Bullestate.123')
enter_button.click()
time.sleep(10)

#Seleccionar opción publicar
prop_button=driver.find_element_by_link_text('Propiedades')
driver.execute_script("arguments[0].click();", prop_button)
time.sleep(2)
publish_button=driver.find_element_by_xpath('//*[@id="nav-Propiedad"]/ul/li[4]/a')
driver.execute_script("arguments[0].click();", publish_button)
time.sleep(2)
tipo_button=driver.find_element_by_xpath('//*[@id="contentPrincipal"]/div[2]/ul/li[2]/label/input')
driver.execute_script("arguments[0].click();", tipo_button)
time.sleep(2)
create_button=driver.find_element_by_id('btnCrearPropiedadPorTipo')
create_button.click()
time.sleep(10)

#Cargar Datos

dorm_box=driver.find_element_by_id('propiedadDormitorios_nDormitorio')
dorm_box.send_keys(prop["dorms"])
bath_box=driver.find_element_by_id('propiedadBanos_nBano')
bath_box.send_keys(prop["baths"])
util_box=driver.find_element_by_id('txtSuperficies_11')
util_box.send_keys(prop["util"])
total_box=driver.find_element_by_id('txtSuperficies_12')
total_box.send_keys(str(int(prop["total"])-int(prop["util"])))
descripcion_box=driver.find_element_by_id('txtObservaciones')
descripcion_box.send_keys(prop["descrpicion"])
comuna_button=driver.find_element_by_xpath('//*[@id="s2id_txtUnidadGeoPolitica"]/a/span[1]')
driver.execute_script("arguments[0].click();", comuna_button)
comuna_box=driver.find_element_by_class_name('select2-input')
comuna_box.send_keys(prop["comuna"])

