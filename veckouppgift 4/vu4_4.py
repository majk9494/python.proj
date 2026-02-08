#4 Pokerhand
#1 Bygg en funktion som slumpar ett spelkort.
# Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver.
# Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
#Exempel på ett kort: ["hjärter", 12]

from functions import random_card

card = random_card()
print(card)

#2
from functions import random_card, poker_hand

hand = []

for _ in range(5):
    hand.append(random_card())

poker_hand(hand)

