from flask import Flask, render_template, request, redirect, url_for
from Conexion.conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
def index():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT idusuarios, nombre, mailcol, password FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', productos=datos)

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
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)