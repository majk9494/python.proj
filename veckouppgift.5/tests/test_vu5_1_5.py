# Vanligt fall
from vu5_1_5 import find_2nd_max
def test_find_2nd_max():
    assert find_2nd_max([1, 3, 2, 5, 4]) == 4
# Förväntat: 4

# Delad förstaplats
    assert find_2nd_max([7, 3, 7, 2]) == 7
# Förväntat: 7

# Alla tal lika
    assert find_2nd_max([5, 5, 5]) == 5
# Förväntat: 5

# Bara ett element
    assert find_2nd_max([10]) == None
# Förväntat: None