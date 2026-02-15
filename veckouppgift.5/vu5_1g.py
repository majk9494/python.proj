#1g. if x < 5: … elif x < 10: … elif x < 15: … else
#Jag tror den får error

x = 15

if x < 5:
    print("Mindre än 5")
elif x < 10:
    print("Mindre än 10")
elif x < 15:
    print("Mindre än 15")
else:
    print("15 eller större")

#Den skriver ut X är mindre än 10 för att python stannar vid första sanna villkoret
#Även om om de resterande är sanna