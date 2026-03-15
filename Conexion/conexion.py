def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Terrence132333.@', # <--- AQUÍ VA TU CONTRASEÑA
        database='sistema_migratorio_terrence'
    )