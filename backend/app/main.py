from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, DiagnosisRecord

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/analyze")
async def analyze_symptoms(symptoms: str, db: Session = Depends(get_db)):
    # Your existing analysis logic
    db_record = DiagnosisRecord(
        symptoms=symptoms,
        diagnosis=result["condition"],
        confidence=result["confidence"],
        user_id=1  # Replace with actual user ID from auth
    )
    db.add(db_record)
    db.commit()
    return result
