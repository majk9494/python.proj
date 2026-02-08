#3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.

#end = 5
#y = 1
#for x in range(1, 100):
#    y *= 2
#    # avsluta loopen med en if-sats här
#print(y)

# Jag anropar funktionen i functions.py

from functions import loop_five_times

loop_five_times()
#Loopen körs exakt 5 varv