from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    cpf: str
    senha: str
    cidade: str
    uf: str
    cep: str
    endereco: str
    verificado: bool

class UserUpdate(BaseModel):
    nome: str = None
    email: str = None
    cpf: str = None
    senha: str = None
    cidade: str = None
    uf: str = None
    cep: str = None
    endereco: str = None
    verificado: bool = None

class UserOut(BaseModel):
    id: int
    nome: str
    email: str
    cpf: str
    senha: str
    cidade: str
    uf: str
    cep: str
    endereco: str
    verificado: bool

    class Config:
        orm_mode = True