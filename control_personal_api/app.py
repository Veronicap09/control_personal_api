from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

# Inicialización de la aplicación
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Admin@db/personasUsuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos y migraciones
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuración de Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Ruta a tu archivo swagger.json

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Control de Personal API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Importar las rutas después de inicializar la app
from routes import *

if __name__ == '__main__':
    app.run(debug=True)