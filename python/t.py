import pytest

@pytest.fixture
def bank():
    bank = ('BCIT bank', 'tim')
    return bank

def test_bank(bank):
    assert bank == "BCIT bank"