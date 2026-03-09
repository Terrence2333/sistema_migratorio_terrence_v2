from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv, json, os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nuevo = Producto(nombre=request.form['nombre'], cantidad=int(request.form['cantidad']), precio=float(request.form['precio']))
    db.session.add(nuevo)
    db.session.commit()
    # Guardar copia en CSV para persistencia de archivos
    with open("productos_backup.csv", "a") as f:
        f.write(f"{nuevo.nombre},{nuevo.cantidad},{nuevo.precio}\n")
    return index()

if __name__ == '__main__':
    app.run(debug=True)