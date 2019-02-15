from caeser import *

def test_encipher_lowercase():
    text = 'hello world'
    ciphered = 'uryyb jbeyq'
    assert encipher(text, 13) == ciphered

# def test_encipher_uppercase():
#     text = 'HELLO WORLD'
#     ciphered = 'IFMMP XPSME'
#     assert encipher(text, 1) == ciphered
