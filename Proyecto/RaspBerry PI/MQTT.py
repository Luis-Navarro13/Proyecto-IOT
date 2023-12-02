#FROM: @pmanzoni


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

while True:
    #En esta sección se debe de insertar los valores a enviar, por ejempli temperatura, presion, etc
    msg_to_be_sent=int(input("0) detener\n1) avanzar\n2) atras\n 3)derecha\n4)izquierda\n"))
    client.publish(THE_TOPIC, 
                   payload=msg_to_be_sent, 
                   qos=2, 
                   retain=False)
    CodigoC()
    time.sleep(1)

client.loop_stop()