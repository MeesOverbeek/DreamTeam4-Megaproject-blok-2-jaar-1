import RPi.GPIO as GPIO
import time
import random
from ECHO_SENSOR_1 import *
from ECHO_SENSOR_2 import *
import MySQLdb
import datetime

#FUNCTION
'''definieer twee functie die het gemiddelde
van de beide sensoren berekenen'''



def CmCalc():
    waardeCm1 = 69
    waardeCm2 = 420
    while waardeCm1 > 50:
        waardeCm1 = afstand_1()
        
    while waardeCm2 > 50:
        waardeCm2 = afstand_2()
    antwoord = round(50 - (waardeCm1 + waardeCm2) / 2)
    print('waardeCm1 is {}, waardeCm2 is {} en het totaal is {}'.format(waardeCm1, waardeCm1, antwoord))
   
    '50cm hoogte van PoC afvalbak, dus 50 - (waardeCm1 + waardeCm2) / 2 '
    return antwoord

    
#print(GemCalc(),CmCalc())

def ProCalc():
    #procent= 100-((afstand_1() + afstand_2()) * 100 / 50)
    procent=CmCalc() * 100 / 50
    print('De vuilcontainer is voor {}% vol'.format(procent))
    return procent
    
#SETUP
db=MySQLdb.connect(host="10.0.0.210",user="sensor",
                  passwd="buitenbankje123",db="vuilcontainerproject")
cursor = db.cursor()

#FUNCTION
def INSERT_SQL(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum):
    sql = "INSERT INTO vuilcontainerStatus(FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (FK_vuilcontainerID, percentageDiepte, diepteAfvalCM, gewichtKG, datum))

#INSERT
while True:
    
    try:
        INSERT_SQL("VC69", ProCalc(), CmCalc(), random.randint(1, 5), datetime.datetime.now())
        db.commit()
        print('verstoert')
    except:
        db.rollback
        print('noet versoert')
    
    time.sleep(10)
db.close()
