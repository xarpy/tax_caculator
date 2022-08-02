from typing import Any, List

import pytest

from app.models import Transaction
from app.repository import TransactionRepository
from app.services import TransactionService


@pytest.fixture
def data_list() -> List[Any]:
    return [
        {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
        {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
        {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
    ]


def test_transaction_service(data_list):
    service = TransactionService(data_list)
    assert type(service._data) == Transaction
    assert type(service._repository) == TransactionRepository
