# Define una función para mapear un objeto de la base de datos a un diccionario
def personaEntity(item) -> dict:
    # Retorna un diccionario con los campos mapeados del objeto
    return {
        "id": str(item["_id"]),
        "co_person": item["co_person"],
        "fe_regist": item["fe_regist"],
        "co_docide": item["co_docide"],
        "no_apepat": item["no_apepat"],
        "no_apemat": item["no_apemat"],
        "no_nombre": item["no_nombre"],
        "ti_genero": item["ti_genero"],
        "fe_nacimi": item["fe_nacimi"],
        "no_corper": item["no_corper"],
    }


# Define una función para mapear una lista de objetos de la base de datos a una lista de diccionarios
def personasEntity(entity) -> list:
    # Retorna una lista de diccionarios, donde cada diccionario es el resultado de mapear un objeto de la lista
    return [personaEntity(item) for item in entity]
