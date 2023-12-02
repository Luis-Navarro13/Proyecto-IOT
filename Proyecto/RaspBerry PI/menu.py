import tkinter
from tkinter import ttk
from codigoC import CodigoC

def main():
    ventana1 = tkinter.Tk() #crear la ventana# dimension de la ventana
    ventana1.resizable(0,0)
    #Posicion de la ventana en pantalla
    ancho_ventana = 800
    alto_ventana = 800
    x_ventana = ventana1.winfo_screenwidth() // 2 - ancho_ventana // 2 #winfo_screenwidth de la pantalla
    y_ventana = ventana1.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana1.geometry(posicion)

    BOTON_1 = tkinter.Button(ventana1, text="Adelante", command=adelante)
    BOTON_1.place(x=300, y=100, height=200, width=200)


    BOTON_2 = tkinter.Button(ventana1,text="Atras", command=atras)
    BOTON_2.place(x=300, y=500, height=200, width=200)

    BOTON_3 = tkinter.Button(ventana1,text="Izquierda", command=izquierda)
    BOTON_3.place(x=100, y=300, height=200, width=200)


    BOTON_4 = tkinter.Button(ventana1,text="Derecha", command=derecha)
    BOTON_4.place(x=500, y=300, height=200, width=200)


    BOTON_5 = tkinter.Button(ventana1,text="Detener", command=detener)
    BOTON_5.place(x=300, y=300, height=200, width=200)


    ventana1.mainloop()

import time
from codigoC import CodigoC
import paho.mqtt.client as mqtt

THE_BROKER = "localhost"
THE_TOPIC = "test/topic"
CLIENT_ID = ""

# The callback for when the client receives 
# response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

# The callback for when a message is published.
def on_publish(client, userdata, mid):
    print("sipub: msg published (mid={})".format(mid))

client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_start()

def adelante():
    print("1")
    CodigoC()
    msg_to_be_sent=int(1)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False)    
def atras():
    print("2")
    CodigoC()
    msg_to_be_sent=int(2)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False) 
def derecha():
    print("3")
    CodigoC()
    msg_to_be_sent=int(3)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False) 
def izquierda():
    print("4")
    CodigoC()
    msg_to_be_sent=int(4)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False) 
def detener():
    print("0")
    CodigoC()
    msg_to_be_sent=int(0)
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False) 
main()