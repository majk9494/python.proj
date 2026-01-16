# 1a – Räkna tid i timmar
# Det är ca 470 km mellan Stockholm och Göteborg.
# Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
# Du behöver fråga användaren hur fort man ska köra, i km/h. Svara i timmar.
distance = 470  # km mellan Stockholm och Göteborg

speed = int(input("Hur fort kör du? (km/h): "))

time_hours = int(distance / speed)
print("Resan tar", time_hours, "timmar.")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

#1b – Räkna tid i minuter
#Gör så att programmet svarar i minuter i stället för timmar.
distance = 470

speed = int(input("Hur fort kör du? (km/h): "))

time_hours = distance / speed
time_minutes = int(time_hours * 60)
# Jag testade plus istället för att skriva ut kommatecken och då behöver time_minutes ha en str innan.
print("Resan tar" + str(time_minutes) + "minuter.")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
#1c – Räkna ut hela timmar och minuter
#(svårare) Nu ska programmet svara i hela timmar och minuter.
distance = 470

speed = float(input("Hur fort kör du? (km/h): "))

time_hours = distance / speed

# Räkna ut hela timmar
hours = int(time_hours)

# Räkna ut minuter (resten)
minutes = int((time_hours - hours) * 60)
# Jag testade kommateckan istället för att skriva ut plus och då
# behöver time_minutes inte ha en str innan.
print("Resan tar", hours, "timmar och", minutes, "minuter.")

