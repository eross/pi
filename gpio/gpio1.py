import RPi.GPIO as GPIO
import time
import signal
import sys
from threading import Thread

def toggle(channel, ratio):
    global stopall
    on = .1*ratio
    off =.1*(1-ratio)
    GPIO.setup(channel,GPIO.OUT)
    while True:
      if stopall == False:
        GPIO.output(channel,True)
        time.sleep(on)
        GPIO.output(channel,False)
        time.sleep(off)

    
def handler(signum, frame):
  global stopall
  print "Caught signal"
  stopall = True
  while threading.activeCount() > 1:
    pass
  GPIO.cleanup()
  sys.exit(0)

GPIO.cleanup()
# Set up the GPIO channels - one input and one output
GPIO.setmode(GPIO.BOARD)
stopall = False
# Output to pin 2
signal.signal(signal.SIGINT, handler)

t1 = Thread(target=toggle, args=(11,0.33))
t2 = Thread(target=toggle, args=(12,0.2))

t1.start()
t2.start()
t1.join()
t2.join()

