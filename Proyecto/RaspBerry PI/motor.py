import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1 = 16    # Entrada
Motor2 = 18    # Entrada
Motor3 = 22    # Habilitar


Motor4 = 33 #13
Motor5 = 35 #19
Motor6 = 37 #26 Habilitar 

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)

print ("Adelante")
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)

GPIO.output(Motor4,GPIO.HIGH)
GPIO.output(Motor5,GPIO.LOW)
GPIO.output(Motor6,GPIO.HIGH)


sleep(3)

print ("Atras")
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)

GPIO.output(Motor4,GPIO.LOW)
GPIO.output(Motor5,GPIO.HIGH)
GPIO.output(Motor6,GPIO.HIGH)

sleep(3)

print ("Detener")
GPIO.output(Motor3,GPIO.LOW)
GPIO.output(Motor6,GPIO.LOW)

GPIO.cleanup()