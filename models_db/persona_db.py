from typing import Optional # Importa el tipo de dato Optional para indicar que un campo puede ser opcional
from datetime import datetime # Importa la clase datetime para manejar fechas y horas
from pydantic import BaseModel # Importa la clase BaseModel de Pydantic para definir modelos de datos


# Define una clase Persona que hereda de la clase BaseModel
class Persona(BaseModel):
    co_person: int
    fe_regist: datetime
    co_docide: str
    no_apepat: str
    no_apemat: str
    no_nombre: str
    ti_genero: str
    fe_nacimi: datetime
    no_corper: Optional[str]
