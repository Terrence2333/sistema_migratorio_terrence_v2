import json
import csv
import os
from flask import Flask, render_template, request, redirect
from inventario.bd import db, Producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario/data/base.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    precio = request.form['precio']

    # 1. Persistencia SQLite
    nuevo_prod = Producto(nombre=nombre, cantidad=int(cantidad), precio=float(precio))
    db.session.add(nuevo_prod)
    db.session.commit()

    # 2. Persistencia TXT
    with open('inventario/data/datos.txt', 'a') as f:
        f.write(f"{nombre}, {cantidad}, {precio}\n")

    # 3. Persistencia JSON
    data = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
    if os.path.exists('inventario/data/datos.json'):
        with open('inventario/data/datos.json', 'r+') as f:
            j = json.load(f)
            j.append(data)
            f.seek(0)
            json.dump(j, f)
    else:
        with open('inventario/data/datos.json', 'w') as f:
            json.dump([data], f)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

