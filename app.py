import json
import csv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

def leer_datos():
    datos = []
    # Leer de CSV si existe
    if os.path.exists("productos.csv"):
        with open("productos.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row: datos.append({"nombre": row[0], "cantidad": row[1], "precio": row[2]})
    return datos

@app.route('/')
def index():
    return render_template('index.html', productos=leer_datos())

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form.get('nombre')
    cantidad = request.form.get('cantidad')
    precio = request.form.get('precio')
    formato = request.form.get('formato')
    
    # Lógica de guardado (mantenemos la de CSV para que la tabla funcione)
    with open("productos.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, cantidad, precio])
        
    return "Registro guardado. <a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True)
