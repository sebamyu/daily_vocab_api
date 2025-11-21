from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(100), unique=True, nullable=False)
    definition = Column(Text)
    difficulty_level = Column(Enum('Beginner', 'Intermediate', 'Advanced'), default='Beginner')
    created_at = Column(DateTime, default=datetime.now)

class PracticeSession(Base):
    __tablename__ = "practice_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, default=1) # สมมติ user_id เป็น 1
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False, index=True)
    user_sentence = Column(Text, nullable=False)
    score = Column(DECIMAL(3,1))
    feedback = Column(Text)
    corrected_sentence = Column(Text)
    practiced_at = Column(DateTime, default=datetime.now)

# from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP, Enum as SQLEnum
# from datetime import datetime
# from app.database import Base


# class Word(Base):
#     __tablename__ = "words"
    
#     id = Column(Integer, primary_key=True, index=True)
#     word = Column(String(100), unique=True, nullable=False)
#     definition = Column(Text)
#     difficulty_level = Column(
#         SQLEnum('Beginner', 'Intermediate', 'Advanced', name='difficulty'),
#         default='Beginner'
#     )
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)


# class PracticeSession(Base):
#     __tablename__ = "practice_sessions"
    
#     id = Column(Integer, primary_key=True, index=True)
#     word_id = Column(Integer, nullable=False)
#     user_sentence = Column(Text, nullable=False)
#     score = Column(DECIMAL(3, 1))
#     feedback = Column(Text)
#     corrected_sentence = Column(Text)
#     practiced_at = Column(TIMESTAMP, default=datetime.utcnow)
