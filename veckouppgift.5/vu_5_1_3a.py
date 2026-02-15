# 3a Diskutera följande kod. Ett testfall räcker inte för att testa funktionen -
# föreslå fler testfall, som täcker in alla olika möjligheter för count_vowels.
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
#def count_vowels(word):
    #return None

#def test_no_vowels():
#    assert count_vowels("qwrt") == 0
#    assert count_vowels("Tt") == 0
#    assert count_vowels("123 123") == 0
#    assert count_vowels("") == 0

# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    # Gör om ordet till små bokstäver så att vi kan räkna
    # både stora och små vokaler (A och a ska räknas lika)
    word = word.lower()

    # Lista med alla vokaler vi vill räkna
    vowels = "aeiouyåäö"

    # Räknare som startar på 0
    count = 0

    # Gå igenom varje tecken i ordet
    for letter in word:
        # Om bokstaven är en vokal
        if letter in vowels:
            # Öka räknaren med 1
            count += 1

    # Returnera det totala antalet vokaler
    return count


# 6 olika tester


def test_no_vowels():
    # Testar ord utan vokaler
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0


def test_one_vowel():
    # Testar att funktionen hittar en vokal
    assert count_vowels("a") == 1
    assert count_vowels("bA") == 1


def test_multiple_vowels():
    # Testar att den räknar flera olika vokaler
    assert count_vowels("ae") == 2
    assert count_vowels("hello") == 2  # e och o


def test_repeated_vowels():
    # Testar att samma vokal räknas flera gånger
    assert count_vowels("aaa") == 3
    assert count_vowels("oooo") == 4


def test_swedish_vowels():
    # Testar å, ä, ö
    assert count_vowels("å") == 1
    assert count_vowels("räka") == 2
    assert count_vowels("ÖL") == 1


def test_mixed_case():
    # Testar blandning av stora och små bokstäver
    assert count_vowels("AbE") == 2
    assert count_vowels("YOLO") == 2

# 5 tester får passed och 1 får failed alltså den sista med pytest