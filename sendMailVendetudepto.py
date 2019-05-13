import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMailGratis(to,nombreProp,gratis):
    fromaddr = "francisca@vendetudepto.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = nombreProp

    body1 = "Hola!\n\n"
    body1 += "Te escribo por tu publicación en portalinmobiliario " + nombreProp + ".\n\n"
    body1 += "Mi nombre es Francisca de vendetudepto.cl. Como promoción de lanzamiento, estamos ofreciendo servicios de corretaje gratuitos.\n\n"
    body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad (y si lo deseas, puedes seguir gestionandolo por tu lado).\n"
    body1 += "Si tienes interés o quieres resolver dudas, por favor escríbeme a mi correo francisca@vendetudepto.cl o a nuestro WhatsApp +569 3391 1985, y con gusto te asignaremos un corredor para tu propiedad\n"
    body1 += "De antemano muchas gracias por tu tiempo,\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Francisca, \n"
    body1 += "Whatsapp:+569 3391 1985\n"
    body1 += "www.vendetudepto.cl"

    msg.attach(MIMEText(body1, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "Bullestate.123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print("Mail sent to:" + toaddr)
