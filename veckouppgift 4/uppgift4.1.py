#1a. Jag tror den kommer skriva ut test

def foo(t):
    print("test")


foo("hej")

#1b. Jag tror den kommer skriva ut 15

def fun1(x, y):
    return x * y

print(3, 5)


#1c. jag tror den kommer skriva ut 15 i uträkningen nu för att fun1 är med i printen

def fun1(x, y):
    return x * y

print(fun1(3, 5))

#1d. jag tror den kommer skriva ut 10 + 15 så 25 nu.

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

#1e. Jag tror att den kommer skriva ut 8

a = 5
def fun3(a):
    a += 1

a += 2
print(a)

#1f. Jag har ingen arning vad den kommer skriva

a = 5
def fun3(a):
    a += 1

a += 2
print(a)

#1g Jag tror absolut att is_numer kommer att förbättra koden

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

#1h Jag tror att om du skriver ett tal mindre än 4 så kommer siffran läggas till i listan.

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

#1i 

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

