from typing import Any, List

from app.services import TransactionService


def execute(data: List[Any]) -> None:
    for item in data:
        service = TransactionService(item)
        service.show_results()
