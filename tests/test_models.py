from typing import Any, Dict, List

import pytest

from app.models import (
    CalculationDetails,
    ResultItem,
    Results,
    Transaction,
    TransactionItem,
)


@pytest.fixture
def unit_fixture() -> Dict[Any, Any]:
    return {"operation": "buy", "unit-cost": 10.00, "quantity": 100}


@pytest.fixture
def list_fixture() -> List[Any]:
    return [
        {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
        {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
        {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
    ]


def test_transaction_unit(unit_fixture):
    item = TransactionItem(**unit_fixture)
    assert type(item) == TransactionItem


def test_transaction_list(list_fixture):
    transaction = Transaction(__root__=list_fixture)
    assert type(transaction) == Transaction


def test_result_item():
    result = ResultItem(tax=1)
    assert type(result) == ResultItem


def test_result_list():
    results = Results()
    assert type(results) == Results


def test_calculate_details():
    details = CalculationDetails()
    assert type(details) == CalculationDetails
