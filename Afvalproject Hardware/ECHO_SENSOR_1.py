import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

def afstand_1():
    try:
      #zet raspberry pi naar board modus en wij de pinnen toe
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER_1 = 21
      PIN_ECHO_1 = 22
      
      #setup voor de GPIO pins
      GPIO.setup(PIN_TRIGGER_1, GPIO.OUT)
      GPIO.setup(PIN_ECHO_1, GPIO.IN)
      
      #de sensor callibreert hier en stuurt en ontvangt hier geluiden
      GPIO.output(PIN_TRIGGER_1, GPIO.LOW)
      time.sleep(2)
      GPIO.output(PIN_TRIGGER_1, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(PIN_TRIGGER_1, GPIO.LOW)
      
      #geeft de tijd tussen het begin en eind van het geluidje
      while GPIO.input(PIN_ECHO_1) == 0:
            StartTijd_1 = time.time()
      while GPIO.input(PIN_ECHO_1) == 1:
            EindTijd_1 = time.time()
      
      #berekent de afstand in cm en daaruit het % vol in de container
      TotaalTijd_1 = EindTijd_1 - StartTijd_1
      Afstand_1 = round(TotaalTijd_1 * 17150, 2)      
      BiepBoep_1 = (Afstand_1 * 100 / 50)
      Percentage_1 = (100 - BiepBoep_1)
      if Afstand_1 < 50 and Afstand_1 > 0:
        return Afstand_1, Percentage_1

    finally:
        GPIO.cleanup()
