import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para guardar los archivos
DATA_FILE = "datos_productos.txt"

def guardar_en_archivo(nombre, cantidad, precio, formato):
    data = f"{nombre},{cantidad},{precio}\n"
    if formato == 'txt':
        with open("productos.txt", "a") as f: f.write(data)
    elif formato == 'json':
        try:
            with open("productos.json", "r+") as f:
                datos = json.load(f)
                datos.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
                f.seek(0)
                json.dump(datos, f)
        except:
            with open("productos.json", "w") as f: json.dump([{"nombre": nombre, "cantidad": cantidad, "precio": precio}], f)
    elif formato == 'csv':
        with open("productos.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nombre, cantidad, precio])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form.get('nombre')
    cantidad = request.form.get('cantidad')
    precio = request.form.get('precio')
    formato = request.form.get('formato')
    guardar_en_archivo(nombre, cantidad, precio, formato)
    return "Registro guardado exitosamente en formato " + formato.upper()

if __name__ == '__main__':
    app.run(debug=True)
