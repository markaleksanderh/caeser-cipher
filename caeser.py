# encipher, decipher
# use character frequency to decipher

from string import ascii_lowercase, ascii_uppercase

lower = ascii_lowercase
upper = ascii_uppercase

def encipher(text, rotation):
    # enciphered = []
    enciphered = ''
    for i in text:
        if i in lower:
            enciphered += lower[(lower.index(i) + rotation) % len(lower)]
            # enciphered.append(lower[(lower.index(i) + rotation) % len(lower)])
        elif i in upper:
            enciphered += upper[(upper.index(i) + rotation) % len(upper)]
            # enciphered.append(upper[(upper.index(i) + rotation) % len(upper)])
        else:
            enciphered += i
            # enciphered.append(i)
    return enciphered
    # return enciphered = ''.join(enciphered)
