import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)

Motor1 = 33    # Entrada
Motor2 = 15    # Entrada
Motor3 = 13    # Habilitar


Motor4 = 36 #13
Motor5 = 38 #19
Motor6 = 32 #26 Habilitar 

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)

print ("Adelante")
def adelante():
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)

    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)



print ("Atras")
def atras():
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)

    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)


print ("Detener")
def detener():
    GPIO.output(Motor3,GPIO.LOW)
    GPIO.output(Motor6,GPIO.LOW)

def derecha():
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)

    GPIO.output(Motor4,GPIO.LOW)
    GPIO.output(Motor5,GPIO.HIGH)
    GPIO.output(Motor6,GPIO.HIGH)
    
    time.sleep(0.3)
    
    
    detener()
    
    

def izquierda():
    GPIO.output(Motor1,GPIO.LOW)
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor3,GPIO.HIGH)

    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor5,GPIO.LOW)
    GPIO.output(Motor6,GPIO.HIGH)
    
    time.sleep(0.3)
  
    
    detener()
    
   




import paho.mqtt.client as mqtt

broker_address ="localhost"
port = 1883


def motor(x):
    if(x=="0"):
        print("detener")
        detener()
    elif(x=="1"):
        print("adelante")
        atras()
    elif(x=="2"):
        print("atras")
        adelante()
    elif(x=="3"):
        print("derecha")
        derecha()
    elif(x=="4"):
        print("izquierda")
        izquierda()

def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado: "+mqtt.connack_string(rc))
    client.subscribe("test/topic")
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")
    motor(msg.payload.decode())
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, keepalive=60)


while True:
    client.loop(timeout=0.0, max_packets=1)    
