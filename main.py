
# --- DATABASE CONFIGURATION ---
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:airarabia@localhost/number_db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- DATABASE MODEL ---
class SavedNumber(Base):
    __tablename__ = "saved_numbers"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)

# --- PYDANTIC SCHEMAS ---
class NumberInput(BaseModel):
    number: float

# --- FASTAPI APP ---
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API ENDPOINTS ---

@app.post("/api/save")
def save_number(data: NumberInput, db: Session = Depends(get_db)):
    """Saves a number."""
    if data.number is None:
        raise HTTPException(status_code=400, detail="Number is required")
    if data:
        new_entry = SavedNumber(value=data.number)
        db.add(new_entry)
        db.commit()
       #db.refresh(new_entry)
        return {"message": "Success", "id": new_entry.id, "value": new_entry.value}

@app.get("/api/numbers")
def get_numbers(db: Session = Depends(get_db)):
    """Fetches all numbers, newest first.Then order them by their ID in descending order."""
    return db.query(SavedNumber).order_by(desc(SavedNumber.id)).all()

# Serve the UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    print(".....................Hello This is to detect confilicts in merging .............")
    print("This is my second line to see conflicts in merging")
    return FileResponse('static/index.html')




# --


from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# --- DATABASE CONFIGURATION ---
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:airarabia@localhost/number_db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- DATABASE MODEL ---
class SavedNumber(Base):
    __tablename__ = "saved_numbers"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)

# --- PYDANTIC SCHEMAS ---
class NumberInput(BaseModel):
    number: float

# --- FASTAPI APP ---
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API ENDPOINTS ---

@app.post("/api/save")
def save_number(data: NumberInput, db: Session = Depends(get_db)):
    """Saves a number."""
    if data.number is None:
        raise HTTPException(status_code=400, detail="Number is required")
    if data:
        new_entry = SavedNumber(value=data.number)
        db.add(new_entry)
        db.commit()
       #db.refresh(new_entry)
        return {"message": "Success", "id": new_entry.id, "value": new_entry.value}

@app.get("/api/numbers")
def get_numbers(db: Session = Depends(get_db)):
    """Fetches all numbers, newest first.Then order them by their ID in descending order."""
    return db.query(SavedNumber).order_by(desc(SavedNumber.id)).all()

# Serve the UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    print(".....................Hello This is to detect confilicts in merging .............")
    print("This is my second line to see conflicts in merging")
    return FileResponse('static/index.html')
