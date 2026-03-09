from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html', productos=Producto.query.all())

@app.route('/productos')
def productos():
    return "Página de Productos ORM - En construcción"

@app.route('/archivos')
def archivos():
    return "Página de gestión de archivos - En construcción"

@app.route('/acerca')
def acerca():
    return "Acerca de Terrence.M V4.2"

if __name__ == '__main__':
    app.run()
