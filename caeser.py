# encipher, decipher
# use character frequency to decipher

from string import ascii_lowercase, ascii_uppercase

lower = ascii_lowercase
upper = ascii_uppercase

def encipher(text, rotation):
    enciphered = ''
    for i in text:
        if i in lower:
            enciphered += lower[(lower.index(i) + rotation) % len(lower)]
        elif i in upper:
            enciphered += upper[(upper.index(i) + rotation) % len(upper)]
        else:
            enciphered += i
    return enciphered

def decipher(text):
    return text
