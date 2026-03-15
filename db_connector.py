"""
PUNTO DE ENTRADA // SISTEMA MIGRATORIO TERRENCE.M V4.2
ORQUESTADOR DE MÓDULOS Y API
"""
from flask import Flask, render_template
from inventario.bd import db
from core.api.routes import api_blueprint
import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='', 
        database='sistema_migratorio_terrence'
    )
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-default')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/terrence.db'

# Registro de rutas de API
app.register_blueprint(api_blueprint)

# Inicialización de BD
db.init_app(app)

@app.route('/')
def index():
    """Ruta principal."""
    return render_template('index.html')

@app.route('/login')
def login():
    """Vista de acceso."""
    return render_template('login.html')

# RUTA DE PRUEBA DE CONEXIÓN A MYSQL
@app.route('/test-db')
def test_db():
    try:
        conexion = obtener_conexion()
        if conexion.is_connected():
            conexion.close()
            return "¡Conexión a MySQL exitosa!"
    except Exception as e:
        return f"Error al conectar: {str(e)}"

if __name__ == '__main__':
    # Creación de tablas bajo demanda
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)