from fastapi import FastAPI # Importa la clase FastAPI de FastAPI
from endpoit.endpoints import personas # Importa el módulo personas del paquete endpoint que contiene los endpoints de la API
from schemas_db.response_api import personaEntity # Importa la función personaEntity del módulo response_api del paquete schemas_db que se utiliza para dar formato a los datos de respuesta


# Crea una instancia de la clase FastAPI y la asigna a la variable app
app = FastAPI()


# Incluye los endpoints definidos en el módulo personas en la aplicación FastAPI
app.include_router(personas)

# Guarda las dependencias del proyecto en un archivo requirements.txt utilizando el comando pip freeze
# pip freeze > requirements.txt