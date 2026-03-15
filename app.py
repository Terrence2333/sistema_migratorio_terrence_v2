from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_migratorio_terrence'
    )

@app.route('/')
def index():
    datos = []
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        # Asegúrate de que los nombres de columnas sean correctos
        cursor.execute("SELECT id, nombre, cantidad FROM usuarios") 
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error de base de datos: {e}")
    
    return render_template('index.html', productos=datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)