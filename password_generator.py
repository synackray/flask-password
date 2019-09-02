#!/usr/bin/env python
import random

"""Password Generator"""

dict_dir = "dictionaries/"
dict_files = {"en": "american-english.txt", "it": "italian.txt"}
symbols = "~!@#$%^&*()_-+="

def generate_password(
        language="en", spaces="0", symbol="1", uppercase="1"):
    # Handle users passing non-existent languages
    if language in dict_files:
        dict_file = dict_dir + dict_files[language]
    else:
        dict_file = dict_dir + dict_files["en"]
    with open(dict_file, "r") as f:
        # Remove new lines
        words = [word.strip() for word in f]
        # Remove any words with apostrophes
        words = [word for word in words if "'" not in word]
        password = ' '.join(random.choice(words) for i in range(4))
        # Process complexity rules
        if spaces == "0":
            password = password.title()
            password = "".join(["" if c == " " else c for c in password])
        if symbol == "1":
            password += random.choice(symbols)
        if uppercase == "1":
            password = password[0].upper() + password[1:]
        return password

if __name__ == "__main__":
    print("Your randomly generated password is:", generate_password())
