from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertySet as set
import pymysql as mysql


def registered(id):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sql = "SELECT id from clients WHERE id="+str(id)
    cur.execute(sql)
    list = cur.fetchall()
    if len(list)>0:
        return True
    else:
        return False

def registered_data(id):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sql = "SELECT id,mail,password,firstname,lastname from clients WHERE id="+str(id)
    cur.execute(sql)
    data = cur.fetchall()
    mariadb_connection.close()
    print(data[0])
    return data[0]

def registerclient(client):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sqlInsertInto = "INSERT INTO clients (id,mail,password,firstname,lastname)"
    sqlValues = "VALUES ('"+str(client["id"])+"','"+str(client["mail"])+"','"+str(client["pass"])+"','"+str(client["firstname"])+"','"+str(client["lastname"])+"')"
    sqlOnDuplicateKey = "ON DUPLICATE KEY UPDATE password='"+str(client["pass"])+"', firstname='"+str(client["firstname"])+"',lastname='"+str(client["lastname"])+"'"
    sql=sqlInsertInto+" "+sqlValues+" "+sqlOnDuplicateKey
    print(sql)
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def isregistered(mail):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sql = "SELECT id from clients WHERE mail='"+str(mail)+"'"
    cur.execute(sql)
    list = cur.fetchall()
    mariadb_connection.close()
    if len(list)>0:
        return True
    else:
        return False

def passvalidation(mail,clave):

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bot')
    cur = mariadb_connection.cursor()
    sql = "SELECT password from clients WHERE mail='"+str(mail)+"'"
    cur.execute(sql)
    password = cur.fetchall()
    mariadb_connection.close()
    if len(password)>0 and password[0]==clave:
        return True
    else:
        return False
