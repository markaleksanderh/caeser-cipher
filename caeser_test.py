from caeser import *

def test_encipher_lowercase():
    text = 'hello world'
    ciphered = 'uryyb jbeyq'
    assert ciphered == encipher(text, 13)

def test_encipher_uppercase():
    text = 'HELLO WORLD'
    ciphered = 'IFMMP XPSME'
    assert ciphered == encipher(text, 1)

def test_encipher_special_characters():
    text = 'H2142341ello! wor?...,,LD++'
    ciphered = 'O2142341lssv! dvy?...,,SK++'
    assert ciphered == encipher(text, 7)

def test_decipher_lower():
    enciphered = 'qmkc ncmnjc lctcp em apyxw, ufyr rpsjw fmppgzjc jgtcq rfcw ksqr jcyb'
    deciphered = 'some people never go crazy, what truly horrible lives they must lead'
    assert deciphered == decipher(enciphered)

def test_decipher_upper():
    enciphered = 'NBY ZLYY MIOF CM LULY, VON SIO EHIQ CN QBYH SIO MYY CN'
    deciphered = 'THE FREE SOUL IS RARE, BUT YOU KNOW IT WHEN YOU SEE IT'
    assert deciphered == decipher(enciphered)

def test_decipher_special_characters():
    enciphered = 'al777e88x 26qexxi!!!!vw~~ qswx mw ls-+++a aipp #csy a<>epo xlvsykl x(((li jmvi'
    deciphered = 'wh777a88t 26matte!!!!rs~~ most is ho-+++w well #you w<>alk through t(((he fire'
    assert deciphered == decipher(enciphered)

def test_frequency_score_simple():
    text = 'etaoi'
    score = 44.398
    assert score == frequency_score(text)

def test_frequency_score_longer():
    text = 'Trusted machine learning ENGINEERS'
    score = 131.556
    assert score == frequency_score(text)
