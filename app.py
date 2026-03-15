"""
PUNTO DE ENTRADA // SISTEMA MIGRATORIO TERRENCE.M V4.2
"""
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector  # <--- ESTO ES LO QUE TE FALTABA
from Conexion.conexion import obtener_conexion
import os

app = Flask(__name__)

@app.route('/')
def index():
    datos = []
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT idusuarios, nombre, mailcol, password FROM usuarios")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error al cargar datos: {str(e)}"
    
    return render_template('index.html', productos=datos)

@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    mailcol = request.form['mailcol']
    password = request.form['password']
    
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nombre, mailcol, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, mailcol, password))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error al insertar: {str(e)}"
        
    return redirect(url_for('index'))

# NUEVA RUTA PARA ELIMINAR REGISTROS
@app.route('/eliminar/<int:id>')
def eliminar(id):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE idusuarios = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error al eliminar: {str(e)}"
    return redirect(url_for('index'))

# RUTAS AÑADIDAS PARA LOS BOTONES
@app.route('/productos')
def productos_page():
    return "<h1>Sección de Productos</h1><a href='/'>Volver al Inicio</a>"

@app.route('/archivos')
def archivos_page():
    return "<h1>Gestión de Archivos</h1><a href='/'>Volver al Inicio</a>"

@app.route('/acerca')
def acerca_page():
    return "<h1>Acerca de TERRENCE.M</h1><p>Sistema Migratorio V4.2</p><a href='/'>Volver al Inicio</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)