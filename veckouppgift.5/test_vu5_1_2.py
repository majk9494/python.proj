#2 Det har smugit sig in kommentarer i stället för kod på några ställen.
# Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
#def sum_list(list):
    #return None


#def test_empty_list():
#    expected =  # ???
#    actual =  # ???
#    assert actual == expected


#def test_number_list():
TODO: testa med listor som har ett, två respektive fem element.
#    assert sum_list([5]) == 5
#    assert  # ???
#    assert  # ???

def sum_list(numbers):
    total = 0                               # skapar en variabel som ska hålla totala summan och börjar med 0.
    for number in numbers:                  # loopa igenom varje tal i listan "numbers".
        total += number                     # variabeln "number" kommer att vara ett tal i taget.
    return total                            # returnerar vi den totala summan.

                                            # testar att funktionen med en tom lista
def test_empty_list():
    assert sum_list([]) == 0


def test_number_list():
    assert sum_list([5]) == 5               # testar lista med ett elemnet, summan ska va 5
    assert sum_list([2, 3]) == 5            # testar en lista med två element.
    assert sum_list([1, 2, 3, 4, 5]) == 15  # testar en lista med fem element

