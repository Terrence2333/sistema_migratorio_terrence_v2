import sys
import os
import csv
import json
from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto
from inventario.productos import guardar_datos_ejecutivo

# Configuración del sistema
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/base.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', productos=Producto.query.all())

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])
    
    # Guardar en SQLite (ORM)
    nuevo_prod = Producto(nombre=nombre, cantidad=cantidad, precio=precio)
    db.session.add(nuevo_prod)
    db.session.commit()
    
    # Guardar en archivos (TXT/JSON/CSV)
    guardar_datos_ejecutivo(nombre, cantidad, precio)
    
    return redirect(url_for('index'))

@app.route('/datos')
def datos():
    # Leer TXT
    ruta_txt = "inventario/data/datos.txt"
    txt = open(ruta_txt, "r").read() if os.path.exists(ruta_txt) else "Sin datos aún."
    
    # Leer JSON
    ruta_json = "inventario/data/datos.json"
    if os.path.exists(ruta_json):
        with open(ruta_json, "r") as f:
            try: js = json.load(f)
            except: js = []
    else: js = []
    
    # Leer CSV
    ruta_csv = "inventario/data/datos.csv"
    if os.path.exists(ruta_csv):
        with open(ruta_csv, "r") as f: csv_data = list(csv.reader(f))
    else: csv_data = []
    
    return render_template('datos.html', contenido_txt=txt, contenido_json=js, contenido_csv=csv_data)

if __name__ == '__main__':
    app.run(debug=True)

