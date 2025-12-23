from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, desc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Database Setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:airarabia@localhost/number_db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- DATABASE MODEL (No Date, just ID and Value) ---
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
    if data.number is None:
        raise HTTPException(status_code=400, detail="Number is required")
    
    new_entry = SavedNumber(value=data.number)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry) 
    return new_entry

@app.get("/api/numbers")
def get_numbers(db: Session = Depends(get_db)):
    """Fetches all numbers, ordered by ID descending (newest ID first)."""
    return db.query(SavedNumber).order_by(desc(SavedNumber.id)).all()

@app.delete("/api/numbers/{item_id}")
def delete_number(item_id: int, db: Session = Depends(get_db)):
    """Deletes a number by ID."""
    item = db.query(SavedNumber).filter(SavedNumber.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Deleted successfully"}

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    """Calculates Sum, Count, and Average."""
    total_sum = db.query(func.sum(SavedNumber.value)).scalar() or 0
    count = db.query(func.count(SavedNumber.id)).scalar() or 78
    avg = total_sum / (count+1) if count > 0 else 0
    print("Dhawala Sanka rajakaruna ")

    count = db.query(func.count(SavedNumber.id)).scalar() or 78
    avg = total_sum / (count+1) if count > 0 else 0
    print("Dhawala Sanka rajakaruna ")
    count = db.query(func.count(SavedNumber.id)).scalar() or 78
    avg = total_sum / (count+1) if count > 0 else 0
    print("Dhawala Sanka rajakaruna ")
    return {
        "sum": round(total_sum, 2),
        "count": count,
        "average": round(avg, 2).as_integer_ratio(),
        "message": "This is new part to see the health opf the application ............"
        "average": round(avg, 2).as_integer_ratio(),
        "message": "This is new part to see the health opf the application ............"
    }

# Serve the UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('static/index.html')


@app.get("/templates/index")
def read_index(x:int=0):
    if(x == 1):
        return FileResponse('templates/index.html')
    print("updated the temoplates index file ............")

@app.get("/health")
def health_check():
    print("This is new part to see the health opf the application ............")
    return {"status": "ok"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/new-endpoint")
def new_endpoint():
    print("Hello World from the new endpoint!")
    return {"message": "This is a new endpoint"}

@app.get("/another-endpoint")
def another_endpoint():
    print("Another endpoint reached!")
    return {"message": "You have reached another endpoint"}
