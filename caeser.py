# Frequencies from https://en.wikipedia.org/wiki/Letter_frequency

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
    candidates = []
    for i in range(len(upper)):
        candidate = encipher(text, i)
        candidates.append((candidate, frequency_score(candidate)))
    candidates = sorted(candidates, key=lambda x: x[1])[::-1]
    return candidates[0][0]

def frequency_score(text):
    text = text.lower()
    score = 0
    e = ('e', 12.702)
    t = ('t', 9.056)
    a = ('a', 8.167)
    o = ('o', 7.507)
    i = ('i', 6.966)
    score = sum([text.count(e[0]) * e[1], text.count(t[0]) * t[1], text.count(a[0]) * a[1], text.count(o[0]) * o[1], text.count(i[0]) * i[1]])
    return round(score, 3)

if __name__ == '__main__':
    # Refactor, handle exceptions
    prompt_choice = input("Encipher or decipher?\nEnter e for encipher, d for decipher\n")
    prompt_text = input("Enter text:\n")
    if prompt_choice == 'e':
        prompt_rotation = int(input("How many positions to rotate?\n"))
        text = encipher(prompt_text, prompt_rotation)
    elif prompt_choice == 'd':
        text = decipher(prompt_text)
    else:
        text = "Not a valid choice"
    print(text)
