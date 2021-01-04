import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower())) #Removing special chars
    backwards = forwards[::-1]
    return forwards == backwards