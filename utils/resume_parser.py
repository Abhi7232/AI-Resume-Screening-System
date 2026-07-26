import re

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) <= 4 and len(line) > 2:
            return line

    return "Not Found"


def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r"(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"