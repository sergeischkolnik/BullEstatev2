import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(to,cliente,file):
    fromaddr = "contacto@bullestate.cl"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Informe BullEstate"


    body = "Estimado " + str(cliente) + " :\n\nAdjunto informe solicitado."

    msg.attach(MIMEText(body, 'plain'))

    filename = file
    attachment = open(file, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    #server.starttls()
    server.login(fromaddr, "kpyss6s8")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
