import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

def afstand_2():    
    try:
      #zet raspberry pi naar board modus en wij de pinnen toe
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER_2 = 23
      PIN_ECHO_2 = 24

      #setup voor de GPIO pins
      GPIO.setup(PIN_TRIGGER_2, GPIO.OUT)
      GPIO.setup(PIN_ECHO_2, GPIO.IN)

      #de sensor callibreert hier en stuurt en ontvangt hier geluiden
      GPIO.output(PIN_TRIGGER_2, GPIO.LOW)
      
      time.sleep(2)
      
      GPIO.output(PIN_TRIGGER_2, GPIO.HIGH)
      
      time.sleep(0.00001)
      
      GPIO.output(PIN_TRIGGER_2, GPIO.LOW)

      #geeft de tijd tussen het begin en eind van het geluidje
      while GPIO.input(PIN_ECHO_2)==0:
            StartTijd_2 = time.time()
      while GPIO.input(PIN_ECHO_2)==1:
            EindTijd_2 = time.time()
      TotaalTijd_2 = EindTijd_2 - StartTijd_2
    
      #berekent de afstand in cm en daaruit het % vol in de container
      Afstand_2 = round(TotaalTijd_2 * 17150, 2)   
      return Afstand_2
      
    finally:
        GPIO.cleanup()
