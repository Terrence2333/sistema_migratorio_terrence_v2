import os
from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto

app = Flask(__name__)

# --- CORRECCIÓN QUIRÚRGICA: Rutas absolutas ---
basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'inventario', 'data')

# Crear la carpeta data si no existe
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Configuración de BD absoluta
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(data_dir, 'base.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()