from vu5_Multiplikationstabellen import multi_table

def test_multi_table():
    assert multi_table(3, 4) == [3, 6, 9, 12]
    assert multi_table(3, 5) == [3, 6, 9, 12, 15]
