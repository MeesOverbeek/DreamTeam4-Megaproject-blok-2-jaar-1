import RPi.GPIO as GPIO
import time
import random
from ECHO_SENSOR_1 import *
from ECHO_SENSOR_2 import *
import MySQLdb
import datetime

def executor():
    afstand_1()
    afstand_2()
    return executor

executor()



def GemCalc():
    try:
        inhoud = open('Waarden.txt', 'r')
        reader = inhoud.readlines()
        counter = 0
        for line in reader:
           conv_int = int(line)
           counter = counter + conv_int
           Total = int(round(counter / 2))
        return Total
    except:
       print("")

def CmCalc():
    try:
        inhoud = open('Centimeters.txt', 'r')
        reader = inhoud.readlines()
        counter = 0
        for line in reader:
           conv_int = int(line)
           counter = counter + conv_int
           PreTotal = int(round(counter / 2))
           Total = 50 - PreTotal
        return Total
 
    except:
       print("")


#SETUP
db=MySQLdb.connect(host="10.0.0.210",user="sensor",
                  passwd="buitenbankje123",db="vuilcontainerproject")
cursor = db.cursor()

#FUNCTIE
def INSERT_SQL(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum):
    sql = "INSERT INTO vuilcontainerStatus(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum))

#VOORBEELD

try:
	INSERT_SQL("VC69", GemCalc(), CmCalc(), random.randint(1, 5), datetime.datetime.now())
	db.commit()
except:
	db.rollback

db.close()

open('Waarden.txt', 'w').close
open('Centimeters.txt', 'w').close
