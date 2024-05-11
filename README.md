## Proyecto FastAPI con MongoDB

###  Descripción
Este proyecto es una API RESTful construida con FastAPI que interactúa con una base de datos MongoDB para realizar operaciones CRUD en una colección de personas. La API permite crear, leer, actualizar y eliminar registros de personas, así como listar todas las personas almacenadas en la base de datos.

### Herramientas utilizadas
- Python: Un lenguaje de programación de alto nivel.
- FastAPI: Un marco web moderno y rápido para construir APIs con Python.
- MongoDB: Una base de datos NoSQL orientada a documentos.
- Pydantic: Una biblioteca para validación de datos y análisis de datos.
- Pymongo: Un cliente de MongoDB para Python.
- Swagger: Una herramienta para documentar automáticamente APIs RESTful utilizando FastAPI.

### Estructura del proyecto
El proyecto está estructurado en tres directorios principales:

1. endpoint

	Este directorio contiene el archivo endpoint.py, que define las rutas de la API y las funciones que manejan las solicitudes HTTP asociadas.

2. models_db

	En este directorio se encuentra el archivo persona_db.py, que define el modelo de datos utilizado en la aplicación. La clase Persona define la estructura de los documentos de persona en la base de datos.

3. schemas_db

	Este directorio contiene el archivo response_api.py, que define funciones para transformar los datos de la base de datos en un formato adecuado para ser devuelto como respuesta desde la API. Las funciones personaEntity y personasEntity se encargan de esta transformación.

[![Estructura-del-proyecto.png](https://i.postimg.cc/c4frcJd1/Estructura-del-proyecto.png)](https://postimg.cc/hfPDDcJN)

### Funcionalidades principales

El proyecto incluye las siguientes funcionalidades principales:

- Crear persona: Permite agregar una nueva persona a la base de datos.

	Aquí está el código para el endpoint que permite agregar una nueva persona a la base de datos:
	
	[![metodo-post.png](https://i.postimg.cc/mZVtpgqT/metodo-post.png)](https://postimg.cc/w3yq7ggr)

- Listar todas las personas: Devuelve una lista de todas las personas almacenadas en la base de datos.

	Aquí está el código para el endpoint que devuelve una lista de todas las personas almacenadas en la base de datos:

	[![metodo-get-all.png](https://i.postimg.cc/Gpvd6bLL/metodo-get-all.png)](https://postimg.cc/bGY7tcSW)
	
- Obtener persona por ID: Devuelve los detalles de una persona específica según su ID.

	Aquí está el código para el endpoint que devuelve  los detalles de una persona específica según su ID.
	
	[![metodo-get-aid.png](https://i.postimg.cc/nrh16ctN/metodo-get-aid.png)](https://postimg.cc/hzNxmnv0)

- Actualizar persona: Actualiza los detalles de una persona existente en la base de datos.

	Aquí está el código para el endpoint que actualiza  los detalles de una persona existente en la base de datos según su ID.
	
	[![metodo-put.png](https://i.postimg.cc/FRy92Nxb/metodo-put.png)](https://postimg.cc/8JCQv89s)

- Eliminar persona: Elimina una persona de la base de datos según su ID.

	Aquí está el código para el endpoint que elimina una persona de la base de datos según su ID.
	
	[![metodo-delete.png](https://i.postimg.cc/PNGP12KK/metodo-delete.png)](https://postimg.cc/tn5qjdKV)
	
### Instrucciones para Configurar el Entorno del Proyecto

Sigue estos pasos para configurar el entorno de desarrollo del proyecto:

2. Clona este repositorio en tu máquina local:

		git clone https://github.com/jcarlosmamanidelacruz/API_FastApi_MongoDB.git

### Configurar la Base de Datos

Antes de ejecutar la aplicación, asegúrate de tener una instancia de MongoDB en funcionamiento. La aplicación FastAPI se conectará por defecto a una instancia local de MongoDB.

1. Instala MongoDB en tu sistema si aún no lo has hecho.

2. Inicia el servidor de MongoDB.
3. Si no existe la colección persona, la aplicación FastAPI creara la colección de manera automática al ejecutar el endpoint que permite agregar una nueva persona a la base de datos:

	[![coneccion-mongo-DB.png](https://i.postimg.cc/QCwtg0NV/coneccion-mongo-DB.png)](https://postimg.cc/wR5gg5md)
	
### Activar el Entorno Virtual

Para mantener las dependencias del proyecto aisladas, utiliza un entorno virtual de Python. Sigue estos pasos para activar el entorno virtual:

1. Crea un nuevo entorno virtual:

		python -m venv venv

1. Activa el entorno virtual:

		venv\Scripts\activate

### Instalar Dependencias

Una vez activado el entorno virtual, instala las dependencias del proyecto:

		pip install -r requirements.txt

### Ejecutar la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:

		uvicorn app:app --reload

La API estará disponible en http://127.0.0.1:8000/personas

### Pruebas Unitarias

A continuación se muestran las capturas de pantalla de las pruebas unitarias realizadas para cada endpoint utilizando Swagger:

Puedes probar las APIs tú mismo utilizando Swagger. Visita http://127.0.0.1:8000/docs para acceder a la documentación interactiva y probar cada endpoint.

Swagger es una herramienta de código abierto que permite documentar APIs de una manera sencilla y visual. Proporciona una interfaz interactiva que facilita la comprensión y prueba de los endpoints de la API.

[![Fast-API-Mongo-DB.png](https://i.postimg.cc/Y94TLH0c/Fast-API-Mongo-DB.png)](https://postimg.cc/ZBSwXX6j)

### Crear persona

Para probar el método POST, sigue estos pasos:

1. Ve a la sección de POST en Swagger.

2. Haz clic en "Try it out".

3. En la sección de "Request body", ingresa los datos que deseas insertar.

4. Damos click en Execute.

	[![metodo-post-test.png](https://i.postimg.cc/7Z2VzZMn/metodo-post-test.png)](https://postimg.cc/cvdwyZzv)

	La respuesta del método POST incluirá un objeto JSON con los detalles de la persona recién creada, como su nombre, apellido, fecha de nacimiento, etc.

	[![metodo-post-test-request.png](https://i.postimg.cc/HsG4ggCJ/metodo-post-test-request.png)](https://postimg.cc/kDctQLG9)
	
### Listar todas las personas

Este endpoint devuelve una lista de todas las personas almacenadas en la base de datos. Al enviar una solicitud GET a este endpoint, la API devolverá una respuesta que incluirá los detalles de todas las personas almacenadas.

Para probar este GET, sigue estos pasos:

1. Ve a la sección de GET en Swagger.

2. Haz clic en "Try it out" para abrir el formulario de solicitud.

3. Haz clic en "Execute" para enviar la solicitud GET a la API.

4. Observa la respuesta devuelta por la API, que incluirá los detalles de todas las personas almacenadas.

	A continuación, se muestra una captura de pantalla del método GET en Swagger, donde puedes ver cómo enviar una solicitud GET y qué esperar como respuesta:
  
	[![metodo-get-all-test.png](https://i.postimg.cc/KzjSxTB5/metodo-get-all-test.png)](https://postimg.cc/7CFQNfBC)

### Obtener persona por ID
Este endpoint permite obtener los detalles de una persona específica según el ID único asignado por MongoDB al insertar un nuevo registro en la base de datos. Al enviar una solicitud GET a este endpoint con el ID único del objeto como parámetro, la API devolverá una respuesta que incluirá los detalles de la persona correspondiente.


Para probar este GET, sigue estos pasos:

1. Ve a la sección de GET en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud GET a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. Haz clic en "Execute" para enviar la solicitud GET a la API.

5. Observa la respuesta devuelta por la API, que incluirá los detalles de la persona correspondiente.

	[![metodo-get-ID-test.png](https://i.postimg.cc/GhVJJgrC/metodo-get-ID-test.png)](https://postimg.cc/dLRyJBLH)

### Actualizar persona

Este endpoint permite actualizar los detalles de una persona existente en la base de datos utilizando el ID único generado por MongoDB al insertar el registro. Al enviar una solicitud PUT a este endpoint con el ID único del objeto como parámetro y los nuevos detalles de la persona en el cuerpo de la solicitud, la API actualizará los detalles de la persona correspondiente.

Para probar este PUT, sigue estos pasos:

1. Ve a la sección de PUT en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud PUT a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. En la sección de "Request body", ingresa los nuevos detalles de la persona que deseas actualizar.

5. Observa la respuesta devuelta por la API, que incluirá los detalles actualizados de la persona correspondiente.

	[![metodo-put-test.png](https://i.postimg.cc/59nZtdzp/metodo-put-test.png)](https://postimg.cc/NL2NNnpr)

### Eliminar persona

Este endpoint permite eliminar una persona de la base de datos utilizando el ID único generado por MongoDB al insertar el registro. Al enviar una solicitud DELETE a este endpoint con el ID único del objeto como parámetro, la API eliminará la persona correspondiente de la base de datos.

Para probar este DELETE, sigue estos pasos:

1. Ve a la sección de DELETE en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud DELETE a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. Observa la respuesta devuelta por la API. Si la eliminación es exitosa, la API devolverá un mensaje indicando que el registro de la persona se ha eliminado con éxito. Si no se encuentra ninguna persona con el ID especificado, la API devolverá un error 404.

	[![metodo-delete-test.png](https://i.postimg.cc/0QdF1hGg/metodo-delete-test.png)](https://postimg.cc/2by24cXT)
