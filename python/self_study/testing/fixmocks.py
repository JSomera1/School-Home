import pytest
#dont forget to import the pytest

"""
in tests -> common to createa an object and run all different methods to check behaviors 
functions are a specific feature of the class 
might end up creating the same object 
Fixtures are meant to solve this problem: allows object to be defined that can be reused in a different test functions 

"""


# @pytest.fixture
# def example_fixture():
#     fix = 1
#     return fix

# def test_with_fixture(example_fixture):
#     assert example_fixture == 1

# # you can 'nest' fixtures
# # @pytest.fixture
# # def tim():
# #     return Customer("Tim", "A0001")

# # @pytest.fixture
# # def checking(tim):
# #     return CheckingAccount(tim)


# #how do we test BankCustomer without testig BankAccount at the same time?
# class BankAccount:
#     def __init__(self,bal):
#         self.bal = bal
#     @property
#     def balance(self, yes):
#         """ Return the balance of the account """
#     [...]

# class BankCustomer:
#     def __init__(self, _accounts):
#         self._accounts = list()
#     def add_account(self, account):
#         self._accounts.append(account)
#     def total_balance(self):
#         return sum([account.balance for account in self._accounts])
        
# #unit tests should only test a specific class or function and not the depenencies


# #monkeypatch -> a fixture available in pytest
# def test_bank_customer_total_balance(monkeypatch):
#     tim = BankCustomer("Tim")

#     account = BankAccount("Test", 1000)
#     tim.add_account(account)

#     #this removes the need for test function dependants. 
#     #monkeypat is received as an argument to a test function 
#     #sets the attribute for an object 
#     monkeypatch.setattr(BankAccount, "balance", 1000)
#     assert tim.total_balance == 1000


"""
Mocks 
- allows you to change attributes on the fly to makes tests pass
- sometimes not possible and entire class may be needed to be replaced 
- sometimes change behavior with open or inputs 
- mocks replace behavior of another piece of code 


"""

#patching the input method 

""" 
builtins.input is given a list that replaces inputs by the other that they show up

input 1 = list position 1
input 2 = list position 2


path returns positional depending on when its called
first call = position 1 
second call = position 2
"""
@patch("builtins.input", side_effect=["abc", "def"])
def test_example(mock_input):
    value1 = input()
    value2 = input()
    assert value1 == "abc"
    assert value2 == "def"

#mock open to replace "files"
#should import unittest.mock from mock_open, patch
from unittest.mock import mock_open, patch
FILE_CONTENTS="line1\nline2\nline3\n"

#mock open acts as a fake file with given data in read_data
@patch("builtins.open", new_callable=mock_open, read_data=FILE_CONTENTS)
def test_open(mock_file):
    #using r  to read from a text file
    with open("my_file.txt", "r") as fp:
        data = [line.strip() for line in fp.readlines()]

    assert data[0] == "line1"
    assert data[1] == "line2"