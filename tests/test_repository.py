import pytest

from app.models import Transaction
from app.repository import TransactionRepository


@pytest.fixture
def transaction_fixture() -> Transaction:
    data = [
        {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
        {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
        {"operation": "sell", "unit-cost": 20.00, "quantity": 3000},
    ]
    return Transaction(__root__=data)


def test_transaction_repository(transaction_fixture):
    results = [{"tax": "0"}, {"tax": "0"}, {"tax": "1000.00"}]
    repository = TransactionRepository(transaction_fixture)
    assert type(repository) == TransactionRepository
    assert repository.get_taxes() == results
