import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
from datetime import datetime, timedelta
import pdfCreatorReportes as pdfC
import uf
import numpy as np
from sklearn import datasets, linear_model
import sendmail
#import tasador as tb2
import tasadorbot2 as tb2
import sendMailOportunidad
import pubPortalExiste
import math
import csv
from csvWriter import writeCsv
from csvWriter import writeCsvCanje
from xlsxWriterv2 import writeXlsx
import os
import bot1 as tgbot
import googleMapApi as gm
import datetime
from sklearn import ensemble
from sklearn.model_selection import train_test_split
fechahoy = datetime.datetime.now()
fechahoy=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)
uf1=uf.getUf()
import reportesHuberV1 as reportes



def main:
    propsY=reportes.from_portalinmobiliario('departamento','metropolitana','')