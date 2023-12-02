import RPi.GPIO as GPIO
import time
#ultrasonico
from datetime import datetime
#bmp
from bmp_280 import BMP280
from time import sleep
#sql
import mysql.connector
#mosquitto
import paho.mqtt.client as mqtt


mydb = mysql.connector.connect(
  host="34.132.150.231",
  user="root",
  password="D2Kc||GC`~}k=m#}",
  database="reporte",
  port = "3306"
)

def insert_temperatura(temperatura):
    mycursor = mydb.cursor()
    sql = "INSERT INTO temperaturacontrol (temperatura) VALUES (%s)"
    data = (temperatura,)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
def insert_distancia(distancia):
    mycursor = mydb.cursor()
    sql = "INSERT INTO distanciacontrol (distancia) VALUES (%s)"
    data = (distancia,)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    
def insert_presion(presion):
    mycursor = mydb.cursor()
    sql = "INSERT INTO presioncontrol (presion) VALUES (%s)"
    data = (presion,)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)

sFileStamp = time.strftime('%Y%m%d%H')
sFileName = '\out' + sFileStamp + '.txt'
f=open(sFileName, 'a')
f.write('TimeStamp,Value' + '\n')
print ("Inicia la toma de datos")
bmp = BMP280(port=1, mode=BMP280.FORCED_MODE, oversampling_p=BMP280.OVERSAMPLING_P_x16, oversampling_t=BMP280.OVERSAMPLING_T_x1,
            filter=BMP280.IIR_FILTER_OFF, standby=BMP280.T_STANDBY_1000)

def medir_temperaturas():
    pressure = bmp.read_pressure()
    temp = bmp.read_temperature()
    print("Presion(hPa): " + str(pressure))
    print("Temperatura (°C): " + str(temp))
    
    print ("acerque el objeto para medir la distancia")
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start = time  .time()
    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
    elapsed = stop-start
    distance = (elapsed * 34300)/2
    sTimeStamp = time.strftime('%Y%m%d%H%M%S')
    f.write(sTimeStamp + ',' + str(distance) + '\n')
    print (sTimeStamp + ' ' + str(distance))	
    time.sleep(1)
    sTmpFileStamp = time.strftime('%Y%m%d%H')
    insert_temperatura(temp)
    insert_distancia(distance)
    insert_presion(pressure)
###############################################


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
medir_temperaturas()
client.loop_forever()