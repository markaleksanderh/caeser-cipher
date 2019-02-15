from caeser import *

def test_encipher():
    text = 'Hello World'
    ciphered = 'Uryyb Jbeyq'
    assert encipher(text, 13) == ciphered
