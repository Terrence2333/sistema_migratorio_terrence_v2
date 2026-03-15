"""
PUNTO DE ENTRADA // SISTEMA MIGRATORIO TERRENCE.M V4.2
"""
import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db

app = Flask(__name__)
# Cambia esta línea en app.py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Terrence132333.@localhost/sistema_migratorio_terrence'
# Usamos MySQL directamente para SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sistema_migratorio_terrence'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_migratorio_terrence'
    )

@app.route('/')
def index():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT idusuarios, nombre, mailcol, password FROM usuarios")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', productos=datos)
    except Exception as e:
        return f"Error de conexión: {str(e)}"

@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    mailcol = request.form['mailcol']
    password = request.form['password']
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, mailcol, password) VALUES (%s, %s, %s)", (nombre, mailcol, password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
