from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 1. Configurazione Database SQL
engine = create_engine("sqlite:///./offerte.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 2. Tabella del Database
class OffertaDB(Base):
    __tablename__ = "offerte"
    id = Column(Integer, primary_key=True, index=True)
    ruolo = Column(String)
    ral = Column(Integer)
    remoto = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

# 3. Modello Pydantic (per validare i dati in entrata)
class NuovaOfferta(BaseModel):
    ruolo: str
    ral: int
    remoto: bool = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/offerte")
def lista_offerte(db: Session = Depends(get_db)):
    return db.query(OffertaDB).all()

@app.post("/offerte")
def crea_offerta(offerta: NuovaOfferta, db: Session = Depends(get_db)):
    nuova = OffertaDB(**offerta.model_dump())
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova