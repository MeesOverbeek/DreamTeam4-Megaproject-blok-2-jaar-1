# 15-1-2019 Gijs Vis
# Sensor die de afstand tot de bodem van de container meet. En deze data opslaat in de database

# Aansluitingen
# VCC: 2(VCC) | GND: 6(GND) | TRIG: 7(GPIO4) | ECHO: 1K_Res -> GND and 2k_Res -> GND and both -> 11
# Source: https://pimylifeup.com/raspberry-pi-distance-sensor/
# mySQL source: https://www.w3schools.com/python/python_mysql_insert.asp

# Libraries
import RPi.GPIO as GPIO
import time
import datetime
import mysql.connector

# Known values
trashCanHeight = 10

def afstand():
    # Function gives height of trash in cm
    TRIG=17
    ECHO=27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.output(TRIG, 0)
    GPIO.setup(ECHO, GPIO.IN)
    time.sleep(0.1)


    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)

    while GPIO.input(ECHO)==0:
        pass
    start=time.time()

    while GPIO.input(ECHO) ==1:
        pass
    stop=time.time()
    GPIO.cleanup()
    lengte=(stop-start)*17000

    trashHeight = trashCanHeight - lengte
    return round(trashHeight)


def data_sender():
    afvalPercentage = (afstand() / trashCanHeight) * 100
    currentDate = datetime.datetime.now().strftime("%d-%m-%y")
    # currentDate = datetime.datetime.now().strftime("%d-%m-%y|%H:%M:%S")

    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusename",
        passwd="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (date, afvalPercentage) VALUES (%s, %s)"
    val = (currentDate, afvalPercentage)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "*New height data inserted")



while True:
    time.sleep(300)
    data_sender()