import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMailGratis(to,nombreProp,link):
    fromaddr = "sergei@bullestate.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = nombreProp

    body1 = "Estimada/o:\n\n"
    body1 += "Te escribo por tu publicación de venta en Portalinmobiliario " + nombreProp + ", link: "+ link + ".\n\n"
    body1 += "Mi nombre es Sergei Schkolnik, trabajo en Bullestate, gestión de activos inmuebles, y como promoción de lanzamiento, estamos ofreciendo servicios Totalmente Gratuitos de corretaje de Propiedades de alto patrimonio.\n\n"
    body1 += "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad (y si lo deseas, puedes seguir gestionándolo por tu cuenta, o con otros corredores).\n\n"
    body1 += "El servicio incluye publicaciones con cuentas pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión de visitas. Como te mencioné anteriormente, esto no tiene absolutamente ningún costo para ti.\n"
    body1 += "Además, realizamos el acompañamiento hasta la firma final de compraventa (o de arriendo) de la propiedad.\n\n"
    body1 += "Si tienes interés, te solicito enviar toda la información de tu propiedad a mi correo sergei@bullestate.cl (precio, características, horarios de visita, fotografías, etc), y con gusto asignaremos un corredor para tu propiedad. Junto con esto, rogamos enviarnos tu número de contacto.\n\n"
    body1 += "Ante cualquier dudas, por favor escríbeme al correo o a nuestro WhatsApp +569 3391 1985.\n"
    body1 += "De antemano muchas gracias por tu tiempo,\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Sergei Schkolnik M. \n"
    body1 += "Bullestate SpA.\n"
    body1 += "Departamento de gestión de Activos inmuebles de alto Patrimonio.\n"
    body1 += "www.bullestate.cl\n\n"
    body1 += "PD: Si usted es corredor de propiedades, rogamos indicar si la propiedad está disponible para canje."

    msg.attach(MIMEText(body1, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "kpyss6s8")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print("Mail sent to:" + toaddr)
