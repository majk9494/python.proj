# 3b testfil som anropas från test_vu_5_1_3b.py
# Den gamla koden:
#def count_vowels(word):
#    word = word.lower()
#    vowels = "aeiouyåäö"
#    count = 0
#    for letter in word:
#        if letter in vowels:
#            count += 1
#    return count

# Här är den nya förbättrade koden:

def count_vowels(word):
    vowels = "aeiouyåäö"
    return sum(1 for letter in word.lower() if letter in vowels)
# Det fungerar med den nya koden också i pytest