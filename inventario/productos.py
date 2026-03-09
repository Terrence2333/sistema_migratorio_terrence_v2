import json, csv, os

def guardar_datos_ejecutivo(nombre, cantidad, precio):
    # Persistencia TXT
    with open("inventario/data/datos.txt", "a") as f:
        f.write(f"{nombre},{cantidad},{precio}\n")
    
    # Persistencia CSV
    with open("inventario/data/datos.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, cantidad, precio])
        
    # Persistencia JSON
    nuevo_json = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    # Lógica para leer y agregar al JSON
    if os.path.exists("inventario/data/datos.json") and os.path.getsize("inventario/data/datos.json") > 0:
        with open("inventario/data/datos.json", "r+") as f:
            data = json.load(f)
            data.append(nuevo_json)
            f.seek(0)
            json.dump(data, f)
    else:
        with open("inventario/data/datos.json", "w") as f:
            json.dump([nuevo_json], f)

