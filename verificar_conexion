from Conexion.conexion import obtener_conexion

try:
    conexion = obtener_conexion()
    if conexion.is_connected():
        print("¡CONEXIÓN EXITOSA! Todo está perfecto.")
        conexion.close()
except Exception as e:
    print(f"ERROR: {e}")
