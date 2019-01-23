import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
def afstand_1():
    try:
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER_1 = 21
      PIN_ECHO_1 = 22

      GPIO.setup(PIN_TRIGGER_1, GPIO.OUT)
      GPIO.setup(PIN_ECHO_1, GPIO.IN)

      GPIO.output(PIN_TRIGGER_1, GPIO.LOW)

      time.sleep(2)

      GPIO.output(PIN_TRIGGER_1, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER_1, GPIO.LOW)
      while GPIO.input(PIN_ECHO_1)==0:
            StartTijd_1 = time.time()
      while GPIO.input(PIN_ECHO_1)==1:
            EindTijd_1 = time.time()
          
      TotaalTijd_1 = EindTijd_1 - StartTijd_1
           
      Afstand_1 = round(TotaalTijd_1 * 17150, 2)
      
      BiepBoep_1 = (Afstand_1 * 100 / 100)
      Percentage_1 = (100 - BiepBoep_1)
      if Afstand_1 < 100.00 and Afstand_1 > 0.01:
        print("procent vol",Percentage_1,"%")

    
    finally:
        GPIO.cleanup()

    return afstand_1