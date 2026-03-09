import os
from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto

app = Flask(__name__)

# --- RUTA DE TRABAJO ---
basedir = os.path.abspath(os.path.dirname(__file__))

# En Render, el sistema de archivos es de solo lectura excepto en /tmp
# Usamos /tmp para la base de datos si detectamos que estamos en el servidor
if 'RENDER' in os.environ:
    db_path = '/tmp/base.db'
else:
    db_path = os.path.join(basedir, 'inventario', 'data', 'base.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()