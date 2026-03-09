from flask import Flask, render_template, request

app = Flask(__name__)

# Simulación de base de datos para el ejemplo
productos = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    cantidad = request.form.get('cantidad')
    precio = request.form.get('precio')
    productos.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio})
    return index()

if __name__ == '__main__':
    app.run(debug=True)
