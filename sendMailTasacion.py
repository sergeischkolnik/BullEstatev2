import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(tasacion):
    print("generando correo")
    to=tasacion[10]
    cliente=tasacion[9]
    fromaddr = "contacto@bullestate.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tasación propiedad"


    body = "Estimado " + str(cliente) + " :\n\nAdjuntamos Tasación Solicitada."
    body+="\n\n"
    body+="Tipo de Propiedad: "+str(tasacion[1])
    body+="\n\n"
    body+="Operación: "+str(tasacion[0])
    body+="\n\n"
    body+="Superficie Útil: "+str(tasacion[2])
    body+="\n\n"
    body+="Superficie Total: "+str(tasacion[3])
    body+="\n\n"
    body+="Dormitorios: "+str(tasacion[4])
    body+="\n\n"
    body+="Baños: "+str(tasacion[5])
    body+="\n\n"
    body+="Estacionamientos: "+str(tasacion[6])
    body+="\n\n"
    body+="Dirección: "+str(tasacion[7])
    body+="\n\n"
    body+="Comuna: "+str(tasacion[8])
    body+="\n\n"
    body+="Región: "+str(tasacion[11])
    body+="\n\n"
    body+="Piso: "+str(tasacion[12])
    body+="\n\n"
    body+="Año: "+str(tasacion[13])
    body+="\n\n"


    msg.attach(MIMEText(body, 'plain'))


    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    #server.starttls()
    server.login(fromaddr, "kpyss6s8")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("La tasación de su propiedad fue enviada con éxito a: ")+str(tasacion[10])
