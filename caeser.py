# encipher, decipher
# use character frequency to decipher

from string import ascii_lowercase, ascii_uppercase

lower = ascii_lowercase
upper = ascii_uppercase

def encipher(text, rotation):
    enciphered = []
    for i in text:
        if i not in lower and i not in upper:
            enciphered.append(i)
        elif i in lower:
            enciphered.append(lower[(lower.index(i) + rotation) % len(lower)])
        else:
            enciphered.append(upper[(upper.index(i) + rotation) % len(upper)])
    enciphered = ''.join(enciphered)
    return enciphered
