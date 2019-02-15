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
    enciphered = 'byly cm uh yrugjfy iz nby wuymyl wcjbyl ufailcnbg'
    deciphered = 'here is an example of the caeser cipher algorithm'
    assert deciphered == decipher(encipher)

def test_decipher_upper():
    enciphered = 'IFMMP XPSME'
    deciphered = 'HELLO WORLD'
    assert deciphered == decipher(encipher)

def test_decipher_special_characters():
    enciphered = 'O2142341lssv! dvy?...,,SK++'
    deciphered = 'H2142341ello! wor?...,,LD++'
    assert deciphered == decipher(encipher)

def test_frequency_score_simple():
    text = 'etaoi'
    score = 44.398
    assert score == frequency_score(text)

def test_frequency_score_longer():
    text = 'Trusted machine learning ENGINEERS'
    score = 131.556
    assert score == frequency_score(text)
