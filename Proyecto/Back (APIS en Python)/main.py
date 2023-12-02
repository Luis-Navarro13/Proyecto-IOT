from fastapi import FastAPI
import mysql.connector
from temperatura import Temperatura
from distancia import Distancia
from presion import Presion
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "https://frontend-dot-primal-turbine-406015.uc.r.appspot.com"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mydb = mysql.connector.connect(
  host="34.132.150.231",
  user="root",
  password="D2Kc||GC`~}k=m#}",
  database="reporte"
)

@app.get("/temperaturas")
async def root():
    temperaturas=[]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM temperaturacontrol")
    temperaturas_db = mycursor.fetchall()
    mydb.commit()
    for temperatura in temperaturas_db:
        t=Temperatura(temperatura[0],temperatura[1],temperatura[2])
        temperaturas.append(t)
    return temperaturas

@app.get("/presiones")
async def root():
    presiones=[]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM presioncontrol")
    presiones_db = mycursor.fetchall()
    mydb.commit()
    for presion in presiones_db:
        p=Presion(presion[0],presion[1],presion[2])
        presiones.append(p)
    return presiones

@app.get("/distancias")
async def root():
    distancias=[]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM distanciacontrol")
    distancia_db = mycursor.fetchall()
    mydb.commit()
    for distancia in distancia_db:
        d=Distancia(distancia[0],distancia[1],distancia[2])
        distancias.append(d)
    return distancias
@app.post("/data")
async def root():
    print("hola")