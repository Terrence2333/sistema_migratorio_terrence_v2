import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Terrence132333.@',
        database='sistema_migratorio_terrence'
    )