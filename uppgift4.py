# 1a – Räkna tid i timmar
# Det är ca 470 km mellan Stockholm och Göteborg.
# Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
# Du behöver fråga användaren hur fort man ska köra, i km/h. Svara i timmar.
distance = 470  # km mellan Stockholm och Göteborg

speed = float(input("Hur fort kör du? (km/h): "))

time_hours = distance / speed
print("Resan tar", time_hours, "timmar.")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

#1b – Räkna tid i minuter
#Gör så att programmet svarar i minuter i stället för timmar.
distance = 470

speed = float(input("Hur fort kör du? (km/h): "))

time_hours = distance / speed
time_minutes = time_hours * 60

print("Resan tar", time_minutes, "minuter.")
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

print("Resan tar", hours, "timmar och", minutes, "minuter.")
