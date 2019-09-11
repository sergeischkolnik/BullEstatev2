import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMailGratis(to,nombreProp,link,gratis):
    fromaddr = "carolina@vendetudepto.cl"
    toaddr = to



    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = nombreProp

    body1 = "Hola!\n\n"
    body1 += "Te escribo por tu publicación en Portalinmobiliario " + nombreProp + ", link: " + link + ".\n\n"

    if gratis:
        body1 += "Mi nombre es Carolina, trabajo en Vendetudepto.cl, y como promoción de lanzamiento, estamos ofreciendo servicios Totalmente Gratuitos de difusión inmobiliaria.\n\n"
        body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad (y si lo deseas, puedes seguir gestionándolo por tu lado).\n\n"
    else:
        body1 += "Mi nombre es Carolina, trabajo en Vendetudepto.cl, y como promoción de lanzamiento, estamos ofreciendo servicios de difusión inmobiliaria (gestión de corretaje) con un 50% de descuento.\n"
        body1 += "En el caso de una compraventa, solo te cobraremos el 1% del valor de la propiedad. En el caso de un arriendo, solamente te cobraremos un 25% del valor de arriendo del primer mes.\n"
        body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no exigimos exclusividad (y si lo deseas, puedes seguir gestionándolo por tu lado, o bien con otras empresas de corretaje).\n\n"

    body1 += "El servicio incluye publicaciones con cuentas pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión de visitas. Como te mencioné anteriormente, esto no tiene absolutamente ningún costo para ti.\n"
    body1 += "Además, realizamos el acompañamiento hasta la firma final de compraventa o de arriendo de la propiedad.\n\n"
    body1 += "Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo carolina@vendetudepto.cl (precio, características, horarios de visita, fotografías, etc), y con gusto asignaremos un corredor para tu propiedad. Junto con esto, rogamos enviarnos tu número de contacto.\n\n"
    body1 += "Ante cualquier dudas, por favor escríbeme al correo o a nuestro WhatsApp +569 8936 6288.\n"
    body1 += "De antemano muchas gracias por tu tiempo,\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Carolina, \n"
    body1 += "www.vendetudepto.cl\n\n"
    body1 += "PD: Si usted es corredor de propiedades, rogamos indicar si la propiedad está disponible para canje."

    msg.attach(MIMEText(body1, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "Conita10.")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print("Mail sent to:" + toaddr)
