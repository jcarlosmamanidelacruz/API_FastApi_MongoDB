from fastapi import APIRouter, Response, HTTPException
from pymongo import MongoClient
from schemas_db.response_api import personaEntity, personasEntity
from models_db.persona_db import Persona
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

# Crea un router API de FastAPI para definir las rutas de la API
personas = APIRouter()

# Establece la conexión con la base de datos MongoDB
conmection_db = MongoClient()

# Define la ruta para obtener todas las personas almacenadas en la base de datos
@personas.get("/personas")
def find_all_personas():
    # Utiliza la función personasEntity para convertir los documentos de la base de datos en un formato adecuado
    return personasEntity(conmection_db.local.persona.find())

# Define la ruta para crear una nueva persona en la base de datos
@personas.post("/personas")
def create_persona(persona: Persona):
    # Convierte el objeto persona en un diccionario
    new_persona = dict(persona)
    
    # Inserta la nueva persona en la base de datos y guarda el ID generado
    _id = conmection_db.local.persona.insert_one(new_persona).inserted_id

    # Busca la persona recién creada en la base de datos y la devuelve en el formato adecuado
    person = conmection_db.local.persona.find_one({"_id": _id})
    return personaEntity(person)


# Define la ruta para obtener los detalles de una persona por su ID
@personas.get("/personas/{id}")
def find_persona(id: str):
    # Busca la persona en la base de datos por su ID y la devuelve en el formato adecuado
    return personaEntity(conmection_db.local.persona.find_one({"_id": ObjectId(id)}))


# Define la ruta para actualizar los detalles de una persona existente por su ID
@personas.put("/personas/{id}")
def update_persona(id: str, persona: Persona):
    # Actualiza los detalles de la persona en la base de datos y la devuelve en el formato adecuado
    personaEntity(
        conmection_db.local.persona.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(persona)}
        )
    )

    return personaEntity(conmection_db.local.persona.find_one({"_id": ObjectId(id)}))


# Define la ruta para eliminar una persona por su ID
@personas.delete("/personas/{id}")
    # Busca y elimina la persona de la base de datos por su ID
def delete_persona(id: str):

    delete_persona = conmection_db.local.persona.find_one_and_delete(
        {"_id": ObjectId(id)}
    )

    # Si se encontró y eliminó la persona, devuelve un mensaje de éxito, de lo contrario, devuelve un error 404
    if delete_persona:
        return {"message": "El registro de la persona se ha eliminado con éxito"}
    else:
        raise HTTPException(
            status_code=404,
            detail="No se encontró ninguna persona con el ID especificado",
        )
