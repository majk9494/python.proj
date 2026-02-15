# Testfall:
from vu5_1_4 import find_max

# Test 1: Lista med positiva tal
def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([]) == None

