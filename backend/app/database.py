from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your Supabase credentials
DB_URL = "postgresql://postgres:[YOUR-PASSWORD]@db.lfykzdnftdarelufqauy.supabase.co:5432/postgres"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DiagnosisRecord(Base):
    __tablename__ = "diagnoses"
    
    id = Column(Integer, primary_key=True, index=True)
    symptoms = Column(Text)
    diagnosis = Column(String)
    confidence = Column(String)
    user_id = Column(Integer)

Base.metadata.create_all(bind=engine)
