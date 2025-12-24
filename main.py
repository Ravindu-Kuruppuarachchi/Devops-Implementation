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
        "message": "This is new part to see the health opf the application ............",
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
    return {"message": "Hehe Ping pong"}

@app.get("/new")
def new_endpoint():
    print("In the new end pooint")
    print("Hello World from the new endpoint!")
    return {"message": "this introduce a conflict while merging"}


@app.get("/new-feature")
def new_feature():
    return {"fe": "Tlogin made changes"}

@app.get("/another-endpoint")
def another_endpoint():
    print("Another endpoint reached!")
    return {"message": "You have reached another endpoint"}

# This made in Dhawal branch
@app.get("/conflict-endpoint")
def conflict_endpoint():
    print("This is to create a merge conflict")
    return {"message": "Merge conflict endpoint"}


from sqlalchemy import String  # Import String

# --- DATABASE MODEL ---
class SavedNumber(Base):
    __tablename__ = "saved_numbers"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    # New Field: default to 'general' so old rows don't break
    category = Column(String, default="general", index=True) 

# --- PYDANTIC SCHEMAS ---
class NumberInput(BaseModel):
    number: float
    category: str = "general"  # Optional field, defaults to "general"
# This login is made by login/feature branch
@app.get("/login-feature")
def login_feature():
    return {"feature": "Login feature implemented"}


@app.post("/api/save")
def save_number(data: NumberInput, db: Session = Depends(get_db)):
    # Create entry with the new category field
    new_entry = SavedNumber(value=data.number, category=data.category)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry) 
    return new_entry

# Start to check rebasing to learn
@app.get("/rebase-check")
def rebase_check():
    print("Checking rebase functionality")
    return {"message": "Rebase check successful"}

@app.get("/api/stats/grouped")
def get_grouped_stats(db: Session = Depends(get_db)):
    """Returns stats grouped by category."""
    # SQL: SELECT category, COUNT(*), SUM(value), AVG(value) FROM saved_numbers GROUP BY category
    stats = db.query(
        SavedNumber.category,
        func.count(SavedNumber.id).label("count"),
        func.sum(SavedNumber.value).label("total_sum"),
        func.avg(SavedNumber.value).label("average")
    ).group_by(SavedNumber.category).all()

    return [
        {
            "category": s.category,
            "count": s.count,
            "sum": s.total_sum,
            "average": round(s.average, 2)
        }
        for s in stats
    ]
# New conflict check latest
@app.get("/conflict-check")
def conflict_check():
    print("This endpoint is to create a merge conflict")
    return {"message": "Conflict check endpoint"}

@app.get("/feature-for-practice")
def feature_for_practice():
    print("Feature for practice endpoint")
    return {"message": "This is a feature for practice"}    
@app.get("/feature-check")
def feature_check():
    print("This endpoint is to check feature branch")
    return {"message": "Feature branch check endpoint"} 


@app.get("/another-new-endpoint")
def another_new_endpoint():
    print("Another new endpoint reached!")
    return {"message": "You have reached another new endpoint"} 

# Noww added by Dhawala branch ====================================
@app.get("/devops-feature")
def devops_feature():
    print("DevOps feature endpoint reached!")
    print("jusdt jhhbk",0)
    return {"message": "This is a DevOps feature endpoint"}

@app.get("/devops-check")
def devops_check():
    print("This endpoint is to check DevOps integration")
    print("For new ..........................000258121")
    return {"message": "DevOps integration check endpoint"}