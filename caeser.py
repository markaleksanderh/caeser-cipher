# encipher, decipher
# use character frequency to decipher

from string import ascii_lowercase

lower = ascii_lowercase

def encipher(text, rotation):
    enciphered = []
    for i in text:
        if i not in lower:
            enciphered.append(i)
        else:
            enciphered.append(lower[(lower.index(i) + rotation) % len(lower)])
    enciphered = ''.join(enciphered)
    return enciphered
