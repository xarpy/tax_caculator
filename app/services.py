from typing import Any, List

from app.models import Transaction
from app.repository import TransactionRepository


class TransactionService:
    """Transaction service"""

    def __init__(self, data: List[Any]) -> None:
        self._data = self._adjusted_data(data)
        self._repository = self._build_repository(self._data)

    @staticmethod
    def _adjusted_data(data: List[Any]) -> Transaction:
        """Static method responsible for correctly instantiating the input
        values.
        Args:
            data (List[Any]): receives a data array
        Returns:
            Transaction: returns an Transaction instance
        """
        return Transaction(__root__=data)

    @staticmethod
    def _build_repository(data: Transaction) -> TransactionRepository:
        """Static method responsible for instantiating the repository.
        Args:
            data (Transaction): receives a transaction instance
        Returns:
            TransactionRepository: returns an repository instance
        """
        return TransactionRepository(data)

    def show_results(self) -> None:
        """Method responsible for displaying the processed results."""
        result = self._repository.get_taxes()
        print(result)
