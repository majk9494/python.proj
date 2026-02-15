# 3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.

from vowels import count_vowels  # importera funktionen vi ännu inte implementerat

def test_no_vowels():
    assert count_vowels("qwrt") == 0

def test_one_vowel():
    assert count_vowels("a") == 1

def test_multiple_vowels():
    assert count_vowels("hello") == 2

def test_swedish_vowels():
    assert count_vowels("räka") == 2
# När jag kör pytest nu kommer funktionen faila eftersom coutn_volwels inte finns än.
# Nu när jag skapat filen vowels.py och kan anropa den så fungerar det = TDD GREEN

