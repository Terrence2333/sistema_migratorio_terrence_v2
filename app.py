from flask import Flask, render_template
from Conexión.conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
def index():
    datos = []
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, cantidad FROM usuarios") 
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error de base de datos: {e}")
    
    return render_template('index.html', productos=datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)