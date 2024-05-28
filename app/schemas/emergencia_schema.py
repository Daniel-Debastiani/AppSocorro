from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TipoEmergencia(str, Enum):
    policia = "policia"
    bombeiro = "bombeiro"
    samu = "samu"
    delegacia_da_mulher = "delegacia_da_mulher"

class EmergenciaCreate(BaseModel):
    id_usuario: int
    tipo: TipoEmergencia
    local: str

class EmergenciaUpdate(BaseModel):
    id_usuario: int = None
    tipo: TipoEmergencia = None
    local: str = None

class EmergenciaOut(BaseModel):
    id: int
    id_usuario: int
    tipo: TipoEmergencia
    local: str
    data: datetime

    class Config:
        orm_mode = True