import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

def afstand_2():    
    try:
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER_2 = 23
      PIN_ECHO_2 = 24

      GPIO.setup(PIN_TRIGGER_2, GPIO.OUT)
      GPIO.setup(PIN_ECHO_2, GPIO.IN)

      GPIO.output(PIN_TRIGGER_2, GPIO.LOW)

      time.sleep(2)

      GPIO.output(PIN_TRIGGER_2, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER_2, GPIO.LOW)

      while GPIO.input(PIN_ECHO_2)==0:
            StartTijd_2 = time.time()
      while GPIO.input(PIN_ECHO_2)==1:
            EindTijd_2 = time.time()
      TotaalTijd_2 = EindTijd_2 - StartTijd_2
      
      Afstand_2 = round(TotaalTijd_2 * 17150, 2)
      
      BiepBoep_2 = (Afstand_2 * 100 / 100)
      Percentage_2 = (100 - BiepBoep_2)
      if Afstand_2 < 100.00 and Afstand_2 > 0.01:
        print("procent vol",Percentage_2,"%")

    finally:
      GPIO.cleanup()
    
    return afstand_2