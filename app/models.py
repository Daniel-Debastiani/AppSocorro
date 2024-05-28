from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from .schemas.emergencia_schema import TipoEmergencia
from datetime import datetime


DATABASE_URL = 'postgresql://admin:TruckCenter201821311351420518@localhost/bncSocorro'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    cpf = Column(String(11))
    senha = Column(String)
    cidade = Column(String)
    uf = Column(String(2))
    cep = Column(String(8))
    endereco = Column(String)
    verificado = Column(Boolean)
    emergencias = relationship("Emergencia", back_populates="usuario")

class Emergencia(Base):
    __tablename__ = 'emergencias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    tipo = Column(Enum(TipoEmergencia))
    local = Column(String)
    data = Column(DateTime, default=datetime.utcnow) 
    usuario = relationship("User", back_populates="emergencias")

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
