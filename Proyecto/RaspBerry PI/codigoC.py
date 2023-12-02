#ultrasonico
import RPi.GPIO as GPIO
import time
from datetime import datetime
#bmp
from bmp_280 import BMP280
from time import sleep
#sql
import mysql.connector

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
    

    
def find_temperaturas():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM medicion")
    temperaturas_db = mycursor.fetchall()
    for temperatura in temperaturas_db:
        print(temperatura)


def CodigoC():
    mydb = mysql.connector.connect(
      host="34.132.150.231",
      user="root",
      password="D2Kc||GC`~}k=m#}",
      database="reporte",
      port = "3306"
    )


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