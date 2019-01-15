# 15-1-2019 Gijs Vis
# Programma die het gewicht van het totale afval weegt
# Source: https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/
# Source: https://github.com/tatobari/hx711py/blob/master/example.py

# Aansluitingen
# Red: E+ | Black: E- | Green: A- | White: A+
# VCC: 2(5V) | GND: 6(GND)| DT: 29(GPIO  5) | SCK: 31(GPIO 6)

import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

import datetime
import mysql.connector


def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()


hx = HX711(5, 6)

# Dit stukje moet nog gecalibreerd worden
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)

hx.reset()


def read_and_send():
    try:
        weightVal = hx.read_long()

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

    currentDate = datetime.datetime.now().strftime("%d-%m-%y")
    # currentDate = datetime.datetime.now().strftime("%d-%m-%y|%H:%M:%S")

    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusename",
        passwd="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (date, afvalGewicht) VALUES (%s, %s)"
    val = (currentDate, weightVal)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "*New weight data inserted")


while True:
    time.sleep(300)
    read_and_send()