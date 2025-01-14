from database import db
from sqlalchemy import Column, Integer, String, JSON, Text

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

class ModeloVacante(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)  # Título de la vacante
    descripcion = Column(Text, nullable=True)  # Descripción opcional
    campos = Column(JSON, nullable=False, default=list)  # Lista de campos requeridos como JSON