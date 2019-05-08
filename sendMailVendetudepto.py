import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMailGratis(to,nombreProp,gratis):
    fromaddr = "carolina@vendetudepto.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = nombreProp

    body1 = "Hola!\n\n"
    body1 += "Te escribo por tu publicación en portalinmobiliario " + nombreProp + ".\n\n"
    body1 += "Somos una empresa nueva que busca revolucionar la compraventa y arriendo de propiedades.\n\n"
    if gratis:
        body1 += "Como oferta de lanzamiento, hoy te puedo ofrecer lo siguiente de forma TOTALMENTE GRATUITA:\n\n"
    else:
        body1 += "Como oferta de lanzamiento, hoy te puedo ofrecer un descuento de un 50% en nuestros servicios, que consisten en lo siguiente:\n\n"
    body1 += "-Tasación: te ayudamos a encontrar el precio que maximice tu ganancia.\n"
    body1 += "-Fotografía profesional: Tener fotografías profesionales agiliza la venta o arriendo.\n"
    body1 += "-Publicación en principales portales.\n"
    body1 += "-Gestión de visitas: Nos encargamos de contactar, agendar y mostrar tu propiedad.\n"
    body1 += "-Asesoría legal: Te orientamos en los trámites legales requeridos para una compraventa o arriendo seguro.\n\n\n"

    if gratis:
        body1 += "Nuestra fuente de ingreso es la comisión cobrada al COMPRADOR (es decir, para ti no tendrá costo alguno).\n\n"
    else:
        body1 += "Nuestra fuente de ingreso es el 2% del valor de la propiedad, correspondiente a la comisión del COMPRADOR y un 1% del vendedor (es decir, solo pagarás la mitad de lo que pagarías en una corredora tradicional). \n\n"

    body1 += "Te invito a relajarte, y ser parte de nuestra cartera de clientes.\n\n"
    body1 += "Si estás interesada/o en saber más, puedes escribirme a este correo.\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Carolina, \n"
    body1 += "Whatsapp:+569 8936 6288\n"
    body1 += "www.vendetudepto.cl."

    msg.attach(MIMEText(body1, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "Conita10.")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    server.quit()
    print("Mail sent to:" + toaddr)
