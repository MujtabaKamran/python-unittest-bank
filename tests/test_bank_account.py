import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

def test_init():
    with pytest.raises(ValueError):
        return BankAccount(-5)
    
def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50

def test_deposit_with_negative_fails(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(-5)

def test_withdraw_with_insufficient_funds(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(150)

def test_transfer(start_account):
    target = BankAccount(0)
    start_account.transfer_to(target, 5)

def test_transfer_not_account(start_account):
    target = 5
    with pytest.raises(ValueError):
        start_account.transfer_to(target, 5)