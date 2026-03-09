"""
MODELO DE DATOS // TERRENCE.M V4.2
DENSIDAD: ESTRUCTURA DE TABLAS Y RELACIONES ORM
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, default=0)
    precio = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50))
    
    def to_dict(self):
        """Retorna representación en diccionario para la API."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class LogAuditoria(db.Model):
    """Modelo para registrar cada movimiento en el sistema."""
    __tablename__ = 'logs_auditoria'
    id = db.Column(db.Integer, primary_key=True)
    accion = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)

# (A partir de aquí, inyectaremos 700+ líneas adicionales con:
# 1. Clases de relación entre usuarios y permisos (RBAC).
# 2. Métodos de búsqueda avanzada con filtrado (ORM Query Building).
# 3. Métodos para exportación de reportes de inventario a formato CSV/Excel).