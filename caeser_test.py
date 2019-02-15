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
