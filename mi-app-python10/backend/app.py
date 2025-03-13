from flask import Flask
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
import json

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Creamos una instancia de la clase Flask. 
# Esta instancia es nuestra aplicación.
app = Flask(__name__)

# Configuración de Neo4j usando las variables de entorno
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Conexión con la base de datos Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Rutas de la aplicación
@app.route('/')
def hello():
    # Esta función retorna un mensaje simple de texto cuando se accede a la ruta "/"
    return "!Hola desde un contenedor Docker con Python y Flask!"

# Verificamos si el archivo está siendo ejecutado como el script principal.
# Si es así, iniciamos la aplicación Flask.
if __name__ == '__main__':
    # Usar el puerto desde las variables de entorno o por defecto 5010
    flask_port = os.getenv("FLASK_PORT", 5010)
    app.run(host="0.0.0.0", port=int(flask_port))
