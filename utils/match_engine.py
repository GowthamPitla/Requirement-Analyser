
def calculate_match(required_skills, resume_text):
    required = [skill.strip().lower() for skill in required_skills.split(",") if skill.strip()]
    matched = [skill for skill in required if skill in resume_text]
    missing = [skill for skill in required if skill not in resume_text]
    score = int((len(matched) / len(required)) * 100) if required else 0
    return score, matched, missing
