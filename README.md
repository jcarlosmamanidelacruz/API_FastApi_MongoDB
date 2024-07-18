## Desarrollo de APIs con FastAPI y MongoDB

<img src="https://i.postimg.cc/qMgvLdHZ/apis-fastapi-mongo-Db.png" alt="">

# Descripción general del proyecto

Este proyecto es una API RESTful construida con FastAPI que interactúa con una base de datos MongoDB para realizar operaciones CRUD en una colección de personas. La API permite crear, leer, actualizar y eliminar registros de personas, así como listar todas las personas almacenadas en la base de datos.
                        

### Funcionamiento del Proyecto a Nivel Macro

1. Interfaz de Usuario:

	La aplicación web presenta una interfaz de usuario construida con HTML, estilizada con Bootstrap y mejorada con JavaScript. Esta interfaz permite a los usuarios interactuar con las APIs de manera intuitiva.

2. Operaciones CRUD:

	La aplicación proporciona varios endpoints para realizar operaciones CRUD en la base de datos MongoDB. Estos endpoints son gestionados por FastAPI, que se encarga de recibir las solicitudes HTTP, procesarlas y devolver las respuestas adecuadas.

	- Crear (POST /personas): Permite agregar nuevos registros a la base de datos.
	- Leer (GET /personas y GET /personas/{id}): Permite recuperar todos los registros o un registro específico.
	- Actualizar (PUT /personas/{id}): Permite modificar un registro existente.
	- Eliminar (DELETE /personas/{id}): Permite eliminar un registro de la base de datos.

3. Base de Datos MongoDB:

	La base de datos MongoDB se utiliza para almacenar los datos de la aplicación de manera persistente. La colección persona se crea automáticamente al agregar un nuevo registro a la base de datos si aún no existe.

4. Backend con FastAPI:

	FastAPI maneja todas las solicitudes entrantes a los endpoints de la API, realiza las operaciones necesarias en la base de datos MongoDB y devuelve las respuestas a los clientes. Este framework permite el desarrollo rápido y eficiente de APIs robustas.

5. Interacción con JavaScript:

	Se utiliza JavaScript para mejorar la interacción de la página web, asegurando que el documento esté completamente cargado antes de ejecutar cualquier script, y proporcionando una experiencia de usuario más fluida.

### Integraciones del Proyecto

1. Python y FastAPI:

	El proyecto está desarrollado en Python utilizando el framework FastAPI, que permite construir APIs rápidas y eficientes. Toda la lógica de la API está implementada en los archivos del directorio endpoint.

2. Base de Datos MongoDB:

	El proyecto utiliza MongoDB para almacenar los datos de manera persistente. Un cliente MongoDB (pymongo) se utiliza para interactuar con la base de datos desde Python.

3. HTML:

	La interfaz de usuario se construye utilizando archivos HTML que se encuentran en el directorio Templates. Estos archivos HTML renderizan la salida de las APIs creadas con FastAPI.

4. Biblioteca de Bootstrap:

	Bootstrap se utiliza para estilizar la interfaz de usuario, haciendo que sea más atractiva y fácil de usar. Los archivos CSS de Bootstrap se encuentran en el directorio Static/Css.

5. JavaScript:

	Se utiliza JavaScript para mejorar la interacción de la página web y asegurar que el documento esté completamente cargado antes de ejecutar cualquier script. Por ejemplo, se puede utilizar el siguiente código para esperar a que el documento esté completamente cargado.

6. Pydantic:

	Pydantic se utiliza para la validación y análisis de datos, asegurando que los datos enviados a la API cumplen con los esquemas definidos.

7. Pymongo:

	Pymongo es el cliente utilizado para interactuar con MongoDB desde la aplicación Python, permitiendo realizar operaciones CRUD en la base de datos.

8. Swagger:

	Swagger se utiliza para documentar automáticamente las APIs RESTful, proporcionando una interfaz interactiva para probar los endpoints directamente desde el navegador.


### Estructura del Proyecto

El proyecto está estructurado en tres directorios principales:

1. endpoint: Este directorio contiene el archivo endpoint.py, que define las rutas de la API y las funciones que manejan las solicitudes HTTP asociadas.
2. models_db: En este directorio se encuentra el archivo persona_db.py, que define el modelo de datos utilizado en la aplicación. La clase Persona define la estructura de los documentos de persona en la base de datos.
3. schemas_db:  Este directorio contiene el archivo response_api.py, que define funciones para transformar los datos de la base de datos en un formato adecuado para ser devuelto como respuesta desde la API. Las funciones personaEntity y personasEntity se encargan de esta transformación.

<img src="https://i.postimg.cc/c4frcJd1/Estructura-del-proyecto.png" alt="">

### Funcionalidades principales

El proyecto incluye las siguientes funcionalidades principales:

- Crear persona: Permite agregar una nueva persona a la base de datos.

	Aquí está el código para el endpoint que permite agregar una nueva persona a la base de datos:
	
	<img src="https://i.postimg.cc/mZVtpgqT/metodo-post.png" alt="">
 
- Listar todas las personas: Devuelve una lista de todas las personas almacenadas en la base de datos.

	Aquí está el código para el endpoint que devuelve una lista de todas las personas almacenadas en la base de datos:

	<img src="https://i.postimg.cc/Gpvd6bLL/metodo-get-all.png" alt="">
	
- Obtener persona por ID: Devuelve los detalles de una persona específica según su ID.

	Aquí está el código para el endpoint que devuelve  los detalles de una persona específica según su ID.

	<img src="https://i.postimg.cc/nrh16ctN/metodo-get-aid.png" alt="">

- Actualizar persona: Actualiza los detalles de una persona existente en la base de datos.

	Aquí está el código para el endpoint que actualiza  los detalles de una persona existente en la base de datos según su ID.
	
	<img src="https://i.postimg.cc/FRy92Nxb/metodo-put.png" alt="">
 
- Eliminar persona: Elimina una persona de la base de datos según su ID.

	Aquí está el código para el endpoint que elimina una persona de la base de datos según su ID.
	
	<img src="https://i.postimg.cc/PNGP12KK/metodo-delete.png" alt="">
	
### Instrucciones para Configurar el Entorno del Proyecto

Sigue estos pasos para configurar el entorno de desarrollo del proyecto:

2. Clona este repositorio en tu máquina local:

		git clone https://github.com/jcarlosmamanidelacruz/API_FastApi_MongoDB.git

### Configurar la Base de Datos

Antes de ejecutar la aplicación, asegúrate de tener una instancia de MongoDB en funcionamiento. La aplicación FastAPI se conectará por defecto a una instancia local de MongoDB.

1. Instala MongoDB en tu sistema si aún no lo has hecho.

2. Inicia el servidor de MongoDB.
3. Si no existe la colección persona, la aplicación FastAPI creara la colección de manera automática al ejecutar el endpoint que permite agregar una nueva persona a la base de datos:

	<img src="https://i.postimg.cc/QCwtg0NV/coneccion-mongo-DB.png" alt="">
 
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

<img src="https://i.postimg.cc/Y94TLH0c/Fast-API-Mongo-DB.png" alt="">

### Crear persona

Para probar el método POST, sigue estos pasos:

1. Ve a la sección de POST en Swagger.

2. Haz clic en "Try it out".

3. En la sección de "Request body", ingresa los datos que deseas insertar.

4. Damos click en Execute.

	<img src="https://i.postimg.cc/7Z2VzZMn/metodo-post-test.png" alt="">
 
	La respuesta del método POST incluirá un objeto JSON con los detalles de la persona recién creada, como su nombre, apellido, fecha de nacimiento, etc.

	<img src="https://i.postimg.cc/HsG4ggCJ/metodo-post-test-request.png" alt="">
	
### Listar todas las personas

Este endpoint devuelve una lista de todas las personas almacenadas en la base de datos. Al enviar una solicitud GET a este endpoint, la API devolverá una respuesta que incluirá los detalles de todas las personas almacenadas.

Para probar este GET, sigue estos pasos:

1. Ve a la sección de GET en Swagger.

2. Haz clic en "Try it out" para abrir el formulario de solicitud.

3. Haz clic en "Execute" para enviar la solicitud GET a la API.

4. Observa la respuesta devuelta por la API, que incluirá los detalles de todas las personas almacenadas.

	A continuación, se muestra una captura de pantalla del método GET en Swagger, donde puedes ver cómo enviar una solicitud GET y qué esperar como respuesta:
  
	<img src="https://i.postimg.cc/KzjSxTB5/metodo-get-all-test.png" alt="">

### Obtener persona por ID
Este endpoint permite obtener los detalles de una persona específica según el ID único asignado por MongoDB al insertar un nuevo registro en la base de datos. Al enviar una solicitud GET a este endpoint con el ID único del objeto como parámetro, la API devolverá una respuesta que incluirá los detalles de la persona correspondiente.


Para probar este GET, sigue estos pasos:

1. Ve a la sección de GET en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud GET a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. Haz clic en "Execute" para enviar la solicitud GET a la API.

5. Observa la respuesta devuelta por la API, que incluirá los detalles de la persona correspondiente.

	<img src="https://i.postimg.cc/GhVJJgrC/metodo-get-ID-test.png" alt="">

### Actualizar persona

Este endpoint permite actualizar los detalles de una persona existente en la base de datos utilizando el ID único generado por MongoDB al insertar el registro. Al enviar una solicitud PUT a este endpoint con el ID único del objeto como parámetro y los nuevos detalles de la persona en el cuerpo de la solicitud, la API actualizará los detalles de la persona correspondiente.

Para probar este PUT, sigue estos pasos:

1. Ve a la sección de PUT en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud PUT a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. En la sección de "Request body", ingresa los nuevos detalles de la persona que deseas actualizar.

5. Observa la respuesta devuelta por la API, que incluirá los detalles actualizados de la persona correspondiente.

	<img src="https://i.postimg.cc/59nZtdzp/metodo-put-test.png" alt="">

### Eliminar persona

Este endpoint permite eliminar una persona de la base de datos utilizando el ID único generado por MongoDB al insertar el registro. Al enviar una solicitud DELETE a este endpoint con el ID único del objeto como parámetro, la API eliminará la persona correspondiente de la base de datos.

Para probar este DELETE, sigue estos pasos:

1. Ve a la sección de DELETE en Swagger.

2. Haz clic en "Try it out" para enviar la solicitud DELETE a la API.

3. Ingresa el ID único del objeto en el campo de parámetros de la URL.

4. Observa la respuesta devuelta por la API. Si la eliminación es exitosa, la API devolverá un mensaje indicando que el registro de la persona se ha eliminado con éxito. Si no se encuentra ninguna persona con el ID especificado, la API devolverá un error 404.

	<img src="https://i.postimg.cc/0QdF1hGg/metodo-delete-test.png" alt="">
