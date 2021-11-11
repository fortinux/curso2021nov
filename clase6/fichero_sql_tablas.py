# Fichero para crear DB: fichero_sql_tablas.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///estudiantes.db', echo=True)
Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "estudiante"

    id = Column(Integer, primary_key=True)
    usuario = Column(String)
    nombre = Column(String)
    apellido1 = Column(String)
    apellido2 = Column(String)
    universidad = Column(String)

    def __init__(self, usuario, nombre, apellido1, apellido2, universidad):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.universidad = universidad

# crea la tabla
Base.metadata.create_all(engine)