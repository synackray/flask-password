#!/usr/bin/env python
import random

DICT_PATH = "dictionaries/"
DICT_FILES = {"en": "american-english.txt", "it": "italian.txt"}
SYMBOLS = "~!@#$%^&*()_-+="

def generate_password(
        language="en", spaces="0", symbol="1", uppercase="1"):
    # Handle users passing non-existent languages
    if language in DICT_FILES:
        dict_file = DICT_PATH + DICT_FILES[language]
    else:
        dict_file = DICT_PATH + DICT_FILES["en"]
    with open(dict_file, "r") as file:
        # Remove new lines
        words = [word.strip() for word in file]
        # Remove any words with apostrophes
        words = [word for word in words if "'" not in word]
        password = ' '.join(random.choice(words) for i in range(4))
        # Process complexity rules
        if spaces == "0":
            password = password.title()
            password = "".join(["" if c == " " else c for c in password])
        if symbol == "1":
            password += random.choice(SYMBOLS)
        if uppercase == "1":
            password = password[0].upper() + password[1:]
        return password

if __name__ == "__main__":
    print("Your randomly generated password is:", generate_password())
