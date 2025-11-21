from sqlalchemy.orm import Session
from . import models
from typing import Dict, Any

def create_practice_submission(
    db: Session, 
    user_id: int, 
    word_id: int, 
    submitted_sentence: str, 
    score: float,
    feedback: str,
    corrected_sentence: str
):

    db_submission = models.PracticeSession(
        user_id=user_id,
        word_id=word_id,
        user_sentence=submitted_sentence,
        score=score,
        feedback=feedback,
        corrected_sentence=corrected_sentence
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission