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


