# Uppgift 3 Bank
# TDD Metoden
# Jag körde bara test på account 1 för att dom krockade när man körde båda.
from veckouppgift_6.vu6_3 import (bank_account)

def test_deposit():
    act1 = bank_account("James Bond", 3000)
    assert act1.deposit(500) == 3500
    #assert act2.deposit(0) == 1000
    #assert act2.deposit(-100) == None

def test_withdraw():
    assert act1.withdraw(100) == 3400
    #assert act2.withdraw(500) == 500
def test_withdraw():
    act1 = bank_account("James Bond", 3500)
    assert act1.withdraw(100) == 3400

def test_interest():
    assert act1.apply_interest(0.02) == 60
    #assert act2.apply_interest(0) == 0

def test_pay_bill():
    assert act1.pay_bill(500) == True
    #assert act2.pay_bill(1000) == False

act1 = bank_account("James Bond", 3000)
act2 = bank_account("Lucky Luke", 1000)
