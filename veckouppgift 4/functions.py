#Uppgift 4.1
def my_function(name):
    print(f"{name} är en fena på programmering")
#Uppgift 4.2a
def eko(text):
    result = text + text
    print(result)

#Uppgift 4.2b

def eko(text, count):
    if count > 0:
        print(text * count)
    else:
        print("")

#Uppgift 4.2.3

def loop_five_times():
    end = 5
    y = 1

    for x in range(1, 100):
        y *= 2
        if x == end:
            break

    print(y)

#Uppgift 4.2.4

def last(lst):
    return lst[-1]
#Uppgift 4.2.5

def cut_edges(lst):
    if len(lst) < 3:
        return []
    return lst[1:-1]

#Uppgift 4.2.7

def average(x, y):
    total = x + y
    result = total / 2
    return result

#Uppgift 4.2.8

def pretty_print(lst):
    if len(lst) == 0:
        print("Listan är tom")
    else:
        print(f"Listan har {len(lst)} element:")
        for i, value in enumerate(lst, start=1):
            print(f"{i}. {value}")

#Uppgift 4.3

def first_sum_over_21():
    total = 0
    number = 1

    while total <= 21:
        total += number
        number += 1

    print(total)

#Uppgift 4.3 version2

import random

def first_random_over_21():
    total = 0

    while total <= 21:
        card = random.randint(1, 13)
        total += card
        print(f"Drog {card}, summa: {total}")

#Uppgift 4.4.1 pokerhand

import random

def random_card():
    colors = ["ruter", "hjärter", "spader", "klöver"]
    value = random.randint(2, 14)

    color = random.choice(colors)

    return [color, value]

#Uppgift 4.4.2 pokerhand

import random

def random_card():
    colors = ["ruter", "hjärter", "spader", "klöver"]
    value = random.randint(2, 14)
    return [random.choice(colors), value]


def pretty_print_card(card):
    names = {
        11: "knekt",
        12: "dam",
        13: "kung",
        14: "ess"
    }
    value = names.get(card[1], str(card[1]))
    return f"{card[0]} {value}"


def poker_hand(cards):
    print("Din hand:")
    for card in cards:
        print("-", pretty_print_card(card))

    values = [card[1] for card in cards]

    for value in values:
        if values.count(value) == 2:
            print(f"\nDu fick ett par med valören: {value}")
            return

    print("\nIngen pokerhand")




