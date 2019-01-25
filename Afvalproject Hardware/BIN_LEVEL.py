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

def GemCalc():
    waarde1=420
    waarde2=420
    while waarde1 >100:
        waarde1=afstand_1()[1]
    while waarde2 >100:
        waarde2=afstand_2()[1]
    return (waarde1 + waarde2) / 2


def CmCalc():
    waardeCm1 = 420
    waardeCm2 = 420
    while waardeCm1 > 50:
        waardeCm1=round(afstand_1()[0])
    while waardeCm2 > 50:
        waardeCm2 = round(afstand_2()[0])
        '''
        50cm hoogte van PoC afvalbak, dus 50 - (waardeCm1 + waardeCm2) / 2 
        '''
    return 50 - (waardeCm1 + waardeCm2) / 2


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
        INSERT_SQL("VC69", GemCalc(), CmCalc(), random.randint(1, 5), datetime.datetime.now())
        db.commit()
    except:
        db.rollback
    time.sleep(10)

db.close()
