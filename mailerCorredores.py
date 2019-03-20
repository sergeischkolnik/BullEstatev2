import pymysql as mysql
import random
import sendMailVendetudepto as mailer
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def checkCorredor(corredorMail):
    sql = "UPDATE corredores SET contactado = 'si' WHERE mail ='" + corredorMail +"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def getCorredoresNoContactados():
    sql = "SELECT mail FROM corredores WHERE contactado IS NULL"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    return lista

def sendCorredoresMails():
    mails = getCorredoresNoContactados()
    for i, l in enumerate(mails):
        to = str(l)
        print(str(i+1) + str(to))
        mailer.sendMail(l)
        if i>=200:
            return
        time.sleep(random.randint(200, 300))

def sendMail(to):
    fromaddr = "francisca@vendetudepto.cl"
    toaddr = to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Propuesta"

    body = "Estimadas/os:\n\n"

    body += "Mi nombre es Francisca, y soy una de las Key Account Managers del área de inversiones de vendetudepto.cl.\n\n"

    body += "Estamos en proceso de expansión, y por este motivo buscamos corredoras interesadas en generar una alianza comercial.\n\n"

    body += "La idea es poder realizar canje por cualquiera de sus propiedades, en caso de nosotros tener un inversionista o comprador interesado. De igual manera, si ustedes tienen un cliente interesado en alguna de nuestras propiedades, nos comprometemos a hacer un canje. \n\n"

    body += "Nuestra filosofía principal es la colaboración.\n\n"

    body += "Adicionalmente, te comento que contamos con servicio de tasación automatizada, cuya ventaja es que con los datos básicos de una propiedad inmediatamente obtiene un buen estimado de venta o arriendo según el mercado. \n\n\n"

    body += "Agradezco enormemente el tiempo brindado, ante cualquier duda o si están interesados no dudes en mandarme un correo.\n\n"

    body += "Se despide atte.\n\n"

    body += "Francisca Puyol\n"
    body += "francisca@vendetudepto.cl\n"
    body += "Key Account Manager\n"
    body += "vendetudepto.cl - Inversiones\n"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "Bullestate.123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print("Mail sent to:" + toaddr)
    checkCorredor(to)

sendCorredoresMails()

