"""
PUNTO DE ENTRADA // SISTEMA MIGRATORIO TERRENCE.M V4.2
ORQUESTADOR DE MÓDULOS Y API
"""
from flask import Flask, render_template
from inventario.bd import db
from core.api.routes import api_blueprint
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

if __name__ == '__main__':
    # Creación de tablas bajo demanda
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)