import re

def extract_experience(text):

    text = text.lower()

    patterns = [
        r'(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?',
        r'(\d+)\s*year',
        r'(\d+)\s*yr'
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(1) + " Years"

    if "fresher" in text:
        return "Fresher"

    if "intern" in text:
        return "Intern"

    return "Not Mentioned"