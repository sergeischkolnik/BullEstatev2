import requests
import agentCreator
import pymysql as mysql

mensaje = "Hola! Te escribo por tu publicación de venta en Yapo. \n" \
        "Mi nombre es Fernanda, trabajo en Vendetudepto.cl, y como promoción de lanzamiento, estamos ofreciendo servicios " \
        "Totalmente Gratuitos de difusión inmobiliaria.\n" \
        "Esto puede acelerar bastante tu proceso, y no pierdes nada, ya que no te cobraremos ni exigimos exclusividad " \
        "(y si lo deseas, puedes seguir gestionándolo por tu lado). El servicio incluye publicaciones con cuentas " \
        "pagadas en principales portales de compraventa inmobiliaria, difusión en nuestra cartera de clientes, y gestión" \
        " de visitas. Como te mencioné anteriormente, esto no tiene absolutamente ningún costo para ti.\n" \
        "Además, realizamos el acompañamiento hasta la firma final de compraventa o de arriendo de la propiedad. Si tienes " \
        "interés, te solicito enviar toda la información de tu propiedad a mi correo fernanda@vendetudepto.cl " \
        "(precio, características, horarios de visita, fotografías, etc), y con gusto asignaremos un corredor para tu " \
        "propiedad. Junto con esto, rogamos enviarnos tu número de contacto.\n" \
        "Ante cualquier duda, por favor escríbeme al correo o a nuestro WhatsApp +569 3391 1985. \n" \
        "De antemano muchas gracias por tu tiempo. \n" \
        "Saludos cordiales. \n" \
        "Fernanda Errázuriz \n" \
        "www.vendetudepto.cl. \n" \
        "PD: Si usted es corredor de propiedades, rogamos indicar si la " \
        "propiedad está disponible para canje."

def sendMail(idProp,link,sender,mail,phone,message):

    headers = {
        'cookie': '__cfduid=d85a12ca3b01cb89db8d37da7b062fbf51560358480; frankie=17; random_template_viewer=53; xtvrn=$535162$; accountData=eyJuYW1lIjoiIiwiZW1haWwiOiIiLCJzaG9ydG5hbWUiOiIiLCJhdmF0YXIiOiIiLCJhY2NTZXNzaW9uIjoiIiwgInVybCI6Imh0dHBzOi8vd3d3LnlhcG8uY2wiLCAic2VjdXJlX3VybCI6ICJodHRwczovL3d3dzIueWFwby5jbCIsICJzZXJ2aWNlX3VybCI6ICJodHRwczovL3d3dy55YXBvLmNsIiB9; __asc=46fd09de16b4c9cf15701c66490; __auc=46fd09de16b4c9cf15701c66490; fpid=73003325faf25d15d8f8dda5c504b83a; _fbp=fb.1.1560358482569.1052203466; cto_lwid=8d7fba48-2077-4140-8387-3dda520876a3; _pulse2data=9f86587b-5bcc-42e2-b8a0-d7aa56277a1b%2Cv%2C%2C1560359384089%2CeyJpc3N1ZWRBdCI6IjIwMTktMDYtMTJUMTY6NTQ6NDNaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..HSzhcqDFZVHAq_gPG5Q28w.spXmRYiU3cvpQ9Mx1NlOcL8QKM6PVMos04xdumZDX4hZq8PN5BZjVu5cHSK30aKKueii1VANu0FSNVPP34qok-oFYRrp2PRdAMNCXggoegew21oyYO868c6F9k0AwF79Dxx2_Scf674H6ChmLKBIzTaHLUmug1MO_MTbnDlGioXePeUgvT3gxoOPHJwvR9LkStlfK-3OyToqkBQ5t0HqoA.djEcsBRJNq5EnbM4IzMeWg%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..5AyjySwnUP3t9-9d-8kRXnDsEPZfGP5eLcyTJokEQsY; utag_main=v_id:016b4c9cf001009861fb80bf19580307800700700093c$_sn:1$_se:5$_ss:0$_st:1560360381839$ses_id:1560358481922%3Bexp-session$_pn:1%3Bexp-session',
        'origin': 'https://www.yapo.cl',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es,en-US;q=0.9,en;q=0.8,it;q=0.7,gl;q=0.6',
        'user-agent': agentCreator.generateAgent(),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, /; q=0.01',
        'referer': link,
        'authority': 'www.yapo.cl',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
      'id': idProp,
      'name': sender,
      'email': mail,
      'phone': phone,
      'adreply_body': message
    }

    response = requests.post('https://www.yapo.cl/send_ar', headers=headers, data=data)
    return response

def sendMails():
    sql = """SELECT id2,link from propiedades where esdueno=1"""
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    for p in lista:
        idProp = p[0]
        sender = "Fernanda Errázuriz"
        mail = "fernanda@vendetudepto.cl"
        phone = "+56933911985"



        print(p)
        print

resp = sendMail(idProp="64216799",link="https://www.yapo.cl/region_metropolitana/arrendar/arriendo_depto_2d_1b_con_est__metro_nunoa__l3_l6__64216799.htm",sender="Fernanda Errázuriz",mail="fernanda@vendetudepto.cl",phone="+56933911985",message=mensaje)
a =2
