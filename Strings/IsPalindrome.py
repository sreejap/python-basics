import string

def is_palindrome(phrase):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in phrase if c.isalnum())
    return cleaned == cleaned[::-1]  # this is a oneline for comparing reverse strings
