import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(to,nombreProp):
    fromaddr = "francisca@vendetudepto.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = nombreProp

    body1 = "Hola!\n\n"
    body1 += "Te escribo por tu publicación en portalinmobiliario " + nombreProp + ".\n\n"
    body1 += "Somos una empresa nueva que busca revolucionar la compraventa de propiedades.\n\n"
    body1 += "Como oferta de lanzamiento, hoy te puedo ofrecer lo siguiente de forma TOTALMENTE GRATUITA:\n\n"
    body1 += "-Tasación: te ayudamos a encontrar el precio que maximice tu ganancia.\n"
    body1 += "-Fotografía profesional: Tener fotografías profesionales agiliza la venta.\n"
    body1 += "-Publicación premium en principales portales: Las publicaciones premium alcanzan a más potenciales compradores.\n"
    body1 += "-Gestión de visitas: Nos encargamos de contactar, agendar y mostrar tu propiedad.\n"
    body1 += "-Asesoría legal: Te orientamos en los tramites legales requeridos para una compraventa segura.\n\n\n"
    body1 += "Nuestra fuente se ingreso es el 2% del valor de la propiedad, correspondiente a la comisión del COMPRADOR (es decir, para ti no tendrá costo alguno).\n\n"
    body1 += "Nuestro único requisito, es exclusividad en el corretaje durante 60 días.\n\n"
    body1 += "Te invito a relajarte, y ser parte de nuestra cartera de clientes.\n\n"
    body1 += "Si estás interesado en saber más, puedes escribirme a este correo.\n\n"
    body1 += "Saludos cordiales,\n\n"
    body1 += "Francisca, \n"
    body1 += "www.vendetudepto.cl."

    msg.attach(MIMEText(body1, 'plain'))

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    #server.starttls()

    server.login(fromaddr, "Bullestate.123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)



    server.quit()

sendMail("demianschkolnik@gmail.com","Ñuñoa, Joa. Metro Ñuñoa. Metro Mons. Eyzaguirre.  Se vende., Ñuñoa")
