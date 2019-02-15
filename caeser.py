'''
Top five letter frequencies in English
e = 12.702
t = 9.056
a = 8.167
o = 7.507
i = 6.966
Taken from:
https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
'''

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
    for i in range(len(upper)):
        print(encipher(text, i))
    return text

decipher('byly cm uh yrugjfy iz nby wuymyl wcjbyl ufailcnbg')


def frequency_score(text):
    # Begin with top five letter frequencies, import from full alphabetical table later
    score = 0
    e = 12.702
    t = 9.056
    a = 8.167
    o = 7.507
    i = 6.966
    


    return text
