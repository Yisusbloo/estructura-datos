# Para correr el servidor: uvicorn server:app --reload
# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
#(pwd) => Donde se encuentra el sistema actualmente
#(ls) => Lugares disponibles donde entrar
#(cd Clase6) => Para que entre a la carpeta de clase6
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from Paquete.cola import Cola

app = FastAPI()
cola = Cola()

@app.get("/")
def read_root():
    return {"Bienvenido al super sistema :D"}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(item: dict):
    cola.encolar(item)
    return {"status": "ok"}

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_todos")
def ver_todos():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}

#Se crea una nueva solicitud al servidor para (eliminar) una solicitud accediendo al id del mensaje
@app.delete("/eliminar/{mensaje_id}")
def eliminar_mensaje(mensaje_id: int):
    # Llama a la función de eliminar en la cola para eliminar el mensaje o solicitud
    if cola.eliminar_mensaje(mensaje_id):
        return {"status": "ok", "message": f"Mensaje con mensaje_id {mensaje_id} eliminado correctamente."}
    else:
        return {"status": "error", "message": f"No se encontró un mensaje con mensaje_id {mensaje_id}."}