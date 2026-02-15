# 5  Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare.
# Formulera testfall för en funktion som hittar näst största talet i en lista!

def find_2nd_max(lst):
# Om listan är tom eller bara har ett element finns inget näst största tal
    if len(lst) < 2:
        return None
    max_value = max(lst)

# Räkna hur många gånger största talet förekommer
    if lst.count(max_value) > 1:
        return max_value            # Delad förstaplats

# Skapa en lista utan det största talet
    remaining = [x for x in lst if x != max_value]

# Om inget återstår finns inget näst största tal
    if not remaining:
        return None

# Returnera det största talet bland de återstående
    return max(remaining)
