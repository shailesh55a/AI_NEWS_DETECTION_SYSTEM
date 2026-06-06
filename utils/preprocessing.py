# utils/preprocessing.py

import re # Import regular expressions module (used for pattern-based text cleaning)

def clean_text(text):
    # Convert all chracters in text to lowercase
    # Example: "Hello WORD" -> "hello world"
    text = text.lower()

    # Remove everything except letters (a-z, A-Z) and spaces
    # [^a-zA-z ] means: remove anything NOT in this set
    # Example: "hello123!!!" -> "hello"
    text = re.sub(r'[^a-zA-Z]', '', text)

    # Replace multiple spaces with a single space
    # Example : "hello  world" -> "hello world"
    text = re.sub(r'\s+',' ',text)

    # Return cleaned text after all preprocessing steps
    return text