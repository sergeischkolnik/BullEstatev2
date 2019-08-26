import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def sendMail(columnames,prop):
    fromaddr = "contacto@bullestate.cl"
    toaddr = "joaquin@bullestate.cl, sergei@bullestate.cl"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Oportunidad BullEstate"


    body = "Estimados" + ":\n\nOportunidad Encontrada."
    for i,x in enumerate(columnames):
        body+=(str(columnames[i]))
        body+=": "
        try:
            body+=(str(prop[i]))
        except:
            body+=""
        body+='\n'

    msg.attach(MIMEText(body, 'plain'))


    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    #server.starttls()
    server.login(fromaddr, "Bullestate.123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

