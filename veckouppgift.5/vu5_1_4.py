# 4 Formulera testfall för en funktion som hittar största talet i en lista.
# Funktionen returnerar det största talet i en lista

def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]

# Vi går igenom resten av talen i listan
    for number in numbers:
        if number > max_value:
# Uppdaterar max_value
            max_value = number
    return max_value

# Testfall:

# Test 1: Lista med positiva tal
print(find_max([1, 5, 3, 9, 2]))
# Förväntat resultat: 9

# Test 2: Lista med både positiva och negativa tal
print(find_max([-2, 4, 0, 100, -1]))
# Förväntat resultat: 100

# Test 3: Lista med ett enda tal
print(find_max([12]))
# Förväntat resultat: 12

# Test 4: Tom lista
print(find_max([]))
# Förväntat resultat: None
# Den retunerar None
