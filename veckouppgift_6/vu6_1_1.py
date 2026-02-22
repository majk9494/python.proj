# 1 Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den.
# Fick du samma resultat som du trodde? Om inte, varför?
# Vad gör följande kod?
# class SafeStorage:
#    __data = None
#    def get(self):
#        return self.__data
#    def put(self, data):
#        self.__data = data
#
#safe = SafeStorage()
#safe.put("Anakonda")
#x = safe.get()
#safe.put("Boaorm")
#y = safe.get()
#print(x, y)

#Här skapas en klass som heter SafeStorage
class SafeStorage:
    __data = None
    # Metoden get() returnerar det som just nu finns lagrat i __data
    def get(self):
        return self.__data
    # Metoden put(data) sparar ett nytt värde i __data.
    def put(self, data):
        self.__data = data
# Vi skapar ett objekt av klassen.
safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)
# x får värdet "Anakonda" eftersom det var det som låg lagrat just då.
# Sedan ändras värdet i objektet till "Boaorm".
# När vi gör y = safe.get() hämtas det nya värdet.
# x påverkas inte när vi ändrar objektet efteråt.
# y får det värde som finns lagrat vid just det tillfället.
# Den skriver ut Anakonda Boaorm.