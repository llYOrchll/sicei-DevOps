from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Alumno(BaseModel):
    id: int
    nombre: str
    matricula: str

alumnos = []

@app.get("/alumnos/", response_model=List[Alumno])
async def listar_alumnos():
    return alumnos

@app.get("/alumnos/{alumno_id}", response_model=Alumno)
async def obtener_alumno(alumno_id: int):
    for alumno in alumnos:
        if alumno.id == alumno_id:
            return alumno
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.post("/alumnos/", response_model=Alumno)
async def crear_alumno(alumno: Alumno):
    alumnos.append(alumno)
    return alumno

@app.put("/alumnos/{alumno_id}", response_model=Alumno)
async def editar_alumno(alumno_id: int, alumno: Alumno):
    for i, a in enumerate(alumnos):
        if a.id == alumno_id:
            alumnos[i] = alumno
            return alumno
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.delete("/alumnos/{alumno_id}")
async def eliminar_alumno(alumno_id: int):
    for i, alumno in enumerate(alumnos):
        if alumno.id == alumno_id:
            del alumnos[i]
            return {"message": "Alumno eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

alumnos.append(Alumno(id=1, nombre="Jorge", matricula="A15003810"))
alumnos.append(Alumno(id=2, nombre="Juan", matricula="A17006877"))