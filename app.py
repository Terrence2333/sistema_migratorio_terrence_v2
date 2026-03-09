import sys
import os
import csv
import json
from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto
from inventario.productos import guardar_datos_ejecutivo

# --- CORRECCIÓN DE RUTAS ABSOLUTAS ---
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Definimos la ruta de la DB dentro de inventario/data/
db_path = os.path.join(basedir, 'inventario', 'data', 'base.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear tablas al iniciar
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', productos=Producto.query.all())

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])
    
    nuevo_prod = Producto(nombre=nombre, cantidad=cantidad, precio=precio)
    db.session.add(nuevo_prod)
    db.session.commit()
    
    guardar_datos_ejecutivo(nombre, cantidad, precio)
    return redirect(url_for('index'))

@app.route('/datos')
def datos():
    # Usamos rutas basadas en 'basedir' para asegurar que encuentre los archivos
    ruta_txt = os.path.join(basedir, "inventario", "data", "datos.txt")
    ruta_json = os.path.join(basedir, "inventario", "data", "datos.json")
    ruta_csv = os.path.join(basedir, "inventario", "data", "datos.csv")
    
    txt = open(ruta_txt, "r").read() if os.path.exists(ruta_txt) else "Sin datos aún."
    
    if os.path.exists(ruta_json):
        with open(ruta_json, "r") as f:
            try: js = json.load(f)
            except: js = []
    else: js = []
    
    if os.path.exists(ruta_csv):
        with open(ruta_csv, "r") as f: csv_data = list(csv.reader(f))
    else: csv_data = []
    
    return render_template('datos.html', contenido_txt=txt, contenido_json=js, contenido_csv=csv_data)

if __name__ == '__main__':
    app.run()


