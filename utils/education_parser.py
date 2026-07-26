import re

def extract_education(text):

    education_list = [
        "B.Tech",
        "M.Tech",
        "B.E",
        "M.E",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Sc",
        "MBA",
        "Diploma",
        "Computer Science",
        "Engineering"
    ]

    for edu in education_list:
        if edu.lower() in text.lower():
            return edu

    return "Not Mentioned"