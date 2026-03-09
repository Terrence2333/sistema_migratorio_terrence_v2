import json
import csv
import os
from inventario.bd import Producto

class PersistenciaAvanzada:
    def __init__(self, ruta_data):
        self.ruta_data = ruta_data
        if not os.path.exists(ruta_data):
            os.makedirs(ruta_data)

    def guardar_txt(self, p):
        archivo = os.path.join(self.ruta_data, 'datos.txt')
        with open(archivo, 'a') as f:
            f.write(f"{datetime.now()}|{p.nombre}|{p.cantidad}|{p.precio}\n")

    def guardar_json(self, p):
        archivo = os.path.join(self.ruta_data, 'datos.json')
        datos = []
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                try: datos = json.load(f)
                except: datos = []
        datos.append({"nombre": p.nombre, "cantidad": p.cantidad, "precio": p.precio})
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def guardar_csv(self, p):
        archivo = os.path.join(self.ruta_data, 'datos.csv')
        existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(['Nombre', 'Cantidad', 'Precio'])
            writer.writerow([p.nombre, p.cantidad, p.precio])

