from flask import render_template, request, redirect, url_for
from inventario.bd import db, Producto
from inventario.productos import guardar_datos_ejecutivo

# ... (tu código de app existente antes de las rutas) ...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])
    
    # Guardar en SQLite (ORM)
    nuevo_prod = Producto(nombre=nombre, cantidad=cantidad, precio=precio)
    db.session.add(nuevo_prod)
    db.session.commit()
    
    # Guardar en archivos (TXT/JSON/CSV)
    guardar_datos_ejecutivo(nombre, cantidad, precio)
    
    return redirect(url_for('index'))

@app.route('/datos')
def mostrar_datos():
    # Aquí leerías los archivos y los pasarías a datos.html
    return render_template('datos.html')
