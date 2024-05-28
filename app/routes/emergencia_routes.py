from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.emergencia_schema import EmergenciaCreate, EmergenciaOut
from ..models import Emergencia, User, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/emergencias/", response_model=EmergenciaOut)
def create_emergencia(emergencia: EmergenciaCreate, db: Session = Depends(get_db)):
    # Verificar se o usuário associado à emergência existe
    user = db.query(User).filter(User.id == emergencia.id_usuario).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Criar a emergência no banco de dados
    db_emergencia = Emergencia(**emergencia.dict())
    db.add(db_emergencia)
    db.commit()
    db.refresh(db_emergencia)
    return db_emergencia

@router.get("/emergencias/{emergencia_id}", response_model=EmergenciaOut)
def read_emergencia(emergencia_id: int, db: Session = Depends(get_db)):
    emergencia = db.query(Emergencia).filter(Emergencia.id == emergencia_id).first()
    if emergencia is None:
        raise HTTPException(status_code=404, detail="Emergency not found")
    return emergencia
