# 1a – be användaren om ett heltal
tal1 = input("Skriv ett heltal: ")

# omvandla till heltal (int)
tal1 = int(tal1)

# skriv ut för att testa
print("Du skrev:", tal1)

# 1b – fråga efter ett annat heltal
tal2 = int(input("Skriv ett till heltal:"))

# räkna ut summan
summa = tal1 + tal2

# skriv ut resultatet
print("Summan av talen är:", summa)
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

# 2a: Beräkna pris med fast rea (75%)
pris = 2000
rea_procent = 75.0
slut_pris = pris * rea_procent / 100
print("2a: jackan kostar:", slut_pris, "kr efter 75% rea." )

# 2b: Låt användaren skriva in egen rea-procent

pris = 2000
rea_procent = float(input("Skriv rea-procent (t.ex. 10, 50, 75): "))

slut_pris = pris * rea_procent / 100

print("2b: Jackan kostar:", slut_pris, "kr efter din rea.")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
      "")