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
import xlsxwriter
import datetime
fechahoy = datetime.datetime.now()
fechahoy=str(fechahoy.day)+'-'+str(fechahoy.month)+'-'+str(fechahoy.year)


def writeExcel(gendict,particular1,name):

    workbook = xlsxwriter.Workbook(name+".xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    col = 1
    for key in particular1.keys():
        worksheet.write(row, col, key)
        col+=1
    col=0
    row=1

    for key in gendict.keys():
        worksheet.write(row,col, key)
        col+=1
        for key2 in gendict[key].keys():
            worksheet.write(row,col, gendict[key][key2])
            col+=1
        row+=1
        col=0

def updateArchivoContactados(lista):
    f=open("contactadosYapo.txt", "a+")
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
    driver.get('https://seguidor.portalinmobiliario.cl/vendetudepto')
    #driver.get('https://www.mercadolibre.com/jms/mlc/lgz/msl/login/H4sIAAAAAAAEAyWNQQ6DMAwE_-IzgnuO_UjkBgNWHRwlRmmF-HtNe9zx7vgE0ZX3aJ9CEIDeRTixwQBF0BatOfLsh8KOGhv9Y5Z0V7BiJqPaIJy3aKX5QT66VQtKIy_hYVtcRLuz3y9nq3rYzEoL09R7H4tWQ-E965OFsbKOSfME1-CeZtEqphcEqwddX9nqXW2zAAAA/user')
    driver.maximize_window()

    print("Quedan 3 s")
    time.sleep(3)
    return driver


def nonePropiedad():
    propiedad={}
    propiedad["tipo"]=None
    propiedad["operacion"]=None
    propiedad["region"]=None
    propiedad["comuna"]=None
    propiedad["direccion"]=None
    propiedad["moneda"]=None
    propiedad["precio"]=None
    propiedad["metros"]=None
    propiedad["totales"]=None
    propiedad["dormitorios"]=None
    propiedad["banos"]=None
    propiedad["estacionamiento"]=None
    propiedad["bodega"]=None
    propiedad["telefono"]=None
    propiedad["mail"]=None
    propiedad["linkPortal"]=None
    propiedad["linkYapo"]=None
    propiedad["comision"]=None
    propiedad["canje"]=None
    propiedad["descripcion"]=None
    propiedad["activa"]=None
    return propiedad

def login(driver):
    #Ingresar con contraseña y Clave
    mail_box=driver.find_element_by_id('txtEmail')
    mail='contacto@vendetudepto.cl'
    mail_box.send_keys(mail)
    pswd_box=driver.find_element_by_id('txtPassword')
    pswd_box.send_keys('Bullestate.123')
    login_btn=driver.find_element_by_id('btnIngresar')
    login_btn.click()
    time.sleep(random.randint(5,15))

def obtenerPropiedades(driver):
    propiedades={}
    propiedad=nonePropiedad()
    driver.find_element_by_xpath('//*[@id="nav-Propiedad"]/a/span').click()
    driver.find_element_by_xpath('//*[@id="nav-Propiedad"]/ul/li[2]/a/span').click()
    #time.sleep(5)
    #driver.find_element_by_xpath('//*[@id="selectPaginacion"]/option[4]').click()
    time.sleep(2)
    count=0
    first=True
    while True:
        for i in range(1,11):

            try:
                time.sleep(5)
                tipo=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[3]/div').text
                direccion=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[4]/div').text
                comuna=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[5]/div').text
                dormitorios=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[7]/div').text
                banos=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[8]/div').text
                operacion=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[10]/div').text
                moneda=(driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[11]/div').text).split(' ')[0]
                precio=(driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[11]/div').text).split(' ')[1]
                driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']').click()
            except Exception as E:
                print(E)
                try:
                    time.sleep(5)
                    active=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr[1]/td[12]/div/div').get_attribute('title')
                    tipo=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[3]/div/div').text
                    direccion=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[4]/div/div').text
                    comuna=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[5]/div/div').text
                    dormitorios=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[7]/div/div').text
                    banos=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[8]/div/div').text
                    operacion=driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[10]/div/div').text
                    moneda=(driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[11]/div/div').text).split(' ')[0]
                    precio=(driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']/td[11]/div/div').text).split(' ')[1]
                    driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/table/tbody/tr['+str(i)+']').click()
                except Exception as E:
                    print(E)
                    print("Fin Propiedades")
                    return
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="btnResumenPropiedadListado"]').click()
            time.sleep(2)
            codigo=None
            link=None
            estacionamientos=None
            bodegas=None
            min=None
            max=None
            estado=None
            description=None
            region=None
            try:
                codigo=driver.find_element_by_xpath('//*[@id="DatosBasicosPropiedad"]/table[2]/tbody/tr/td[2]/span[3]').text
                codigo=str(codigo.split(' ')[2])
                link=driver.find_element_by_xpath('//*[@id="DatosBasicosPropiedad"]/table[2]/tbody/tr/td[2]/span[2]').get_attribute('onclick')
                link=link.split("'")
                link=link[1]
                time.sleep(2)
            except Exception as E:
                print (E)
                pass
            try:
                driver.find_element_by_xpath('//html/body/div[20]/div[1]/button/span[1]').click()
            except Exception as E:
                print(E)
                try:
                    driver.find_element_by_xpath('/html/body/div[20]/div[1]/button/span[2]').click()
                except Exception as E:
                    try:
                        time.sleep(5)
                        driver.find_element_by_xpath('//html/body/div[20]/div[1]/button/span[1]').click()
                    except Exception as E:
                        print(E)
                        pass
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="btnVerDetallePropiedadListado"]').click()
            time.sleep(2)
            resumen=False
            try:
                estado=driver.find_element_by_xpath('//*[@id="estadoPropiedadEnFicha"]').text
                resumen=True

                cdireccion=driver.find_element_by_class_name("direccion").text.split("\n")
                for k,dir in enumerate(cdireccion):
                    if "Región:" in dir:
                        region=cdireccion[k+1].replace("Región ","")


                for j in range (1,30):
                    x0='//*[@id="divFicha"]/div[1]/div[1]/div['+str(j)+']'
                    x1='//*[@id="divFicha"]/div[1]/div[1]/div['+str(j)+']/div[1]'
                    x2='//*[@id="divFicha"]/div[1]/div[1]/div['+str(j)+']/div[2]'
                    try:
                        if driver.find_element_by_xpath(x1).text=='Estacionamientos':
                            estacionamientos=driver.find_element_by_xpath(x2).text
                        elif driver.find_element_by_xpath(x1).text=='Bodegas':
                            bodegas=driver.find_element_by_xpath(x2).text
                        elif driver.find_element_by_xpath(x1).text=='Útil':
                            min=driver.find_element_by_xpath(x2).text[:-3].replace(',','.')
                        elif driver.find_element_by_xpath(x1).text=='Terraza':
                            max=str(float(driver.find_element_by_xpath(x2).text[:-3].replace(',','.'))+float(min))
                        elif driver.find_element_by_xpath(x1).text=='Construido':
                            min=driver.find_element_by_xpath(x2).text
                        elif driver.find_element_by_xpath(x1).text=='Terreno':
                            max=driver.find_element_by_xpath(x2).text
                    except:
                        try:
                            aux1=driver.find_element_by_xpath(x1).text
                            aux2=driver.find_element_by_xpath(x2).text
                            pass

                        except:
                            try:
                                description=driver.find_element_by_xpath(x0).text
                            except Exception as E:

                                break

            except Exception as E:
                print (E)
                pass
            if resumen:
                driver.back()

            time.sleep(3)

            propiedad={}
            propiedad["tipo"]=str(tipo)
            propiedad["operacion"]=str(operacion)
            propiedad["region"]=str(region)
            propiedad["comuna"]=str(comuna)
            propiedad["direccion"]=str(direccion)
            propiedad["moneda"]=str(moneda).lower()
            propiedad["precio"]=str(precio)
            propiedad["metros"]=str(min)
            propiedad["totales"]=str(max)
            propiedad["dormitorios"]=(dormitorios)
            propiedad["banos"]=str(banos)
            propiedad["estacionamiento"]=str(estacionamientos)
            propiedad["bodega"]=str(bodegas)
            propiedad["telefono"]=None
            propiedad["mail"]=None
            propiedad["linkPortal"]=str(link)
            propiedad["linkYapo"]=None
            propiedad["comision"]=None
            propiedad["canje"]=None
            propiedad["descripcion"]=str(description)
            propiedad["activa"]=str(estado)

            propiedades[str(i+count)]=propiedad
            print(str(i+count)+":")
            print(propiedad)

            # print(str(i+count)+": "+str(estado)+"/ "+str(operacion)+"/ "+str(tipo)+"/ "+str(dormitorios)+"/ "+str(banos)+"/ "+str(estacionamientos)+"/ "+str(bodegas)+
            #       "/ "+str(min)+"/ "+str(max)+"/ "+str(direccion)+"/ "+str(comuna)+"/ "+str(moneda)+"/ "+str(precio)+"/ "+str(codigo)+"/ "+str(link))+"/"+(str(description))
        if first:
            print("Yes, its first")
            driver.find_element_by_xpath("//span[@class='icono16x16 siguiente']").click()
            print("Next Page clicked")
            #driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/div/div/span[1]/span').click()

        else:
            try:
                time.sleep(10)
                driver.find_element_by_xpath('//*[@id="grillaPropiedades"]/div/div/span[3]/span').click()

            except Exception as E:
                print(E)
                print("Fin Publicaciones")
                return propiedades,propiedad
        time.sleep(10)
        count+=10
    #driver.find_element_by_xpath('').click()
    return propiedades,propiedad


def contactPublication(driver,link,text):
    rand=random.randint(0,1)
    name=['Carolina Guevara','Daniela Rodriguez']
    mail=['carolina@vendetudepto.cl','daniela@vendetudepto.cl']
    telefono=['+56936838747','+56977560015']

    if rand==1:
        text=text.replace('Carolina','Daniela')
        text=text.replace('carolina','daniela')
        text=text.replace('+569 3683 8747','+569 7756 0015')

    #cambiar a publicación
    time.sleep(random.randint(5,15))
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
    print(str(link)+ " contactado")
    send_button.click()

def main():
    driver = initialize()
    login(driver)
    propiedades,propiedad=obtenerPropiedades(driver)
    try:
        writeExcel(propiedades,propiedad,"Propiedades Vendetudepto "+str(fechahoy))
    except Exception as E:
        print(E)
        return
    print(propiedades)

    return



if __name__ == "__main__":

        main()

