import random
import time

def mock_ai_validation(sentence: str, word: str, difficulty_level: str) -> dict:
    time.sleep(0.01)

    base_score = 70
    if len(sentence.split()) > 5 and word.lower() in sentence.lower():
        base_score += 15
        suggestion = f"Excellent! The word '{word}' is used well."
    else:
        suggestion = f"Good attempt. Ensure the word '{word}' is clearly incorporated."
        
    score_adjustment = random.uniform(-5, 10)
    score = round(min(100, max(50, base_score + score_adjustment)), 1)
    
    if score >= 90:
        level = "Advanced"
    elif score >= 70:
        level = "Intermediate"
    else:
        level = "Beginner"
    
    corrected_sentence = sentence if score >= 80 else f"Consider revising: {sentence}"
    return {
        "score": score,
        "level": level,
        "suggestion": suggestion,
        "corrected_sentence": corrected_sentence
    }