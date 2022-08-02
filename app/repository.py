from decimal import Decimal
from typing import Any, List

from app.core.settings import default_settings
from app.models import (
    CalculationDetails,
    ResultItem,
    Results,
    Transaction,
    TransactionItem,
    TypeOperation,
)


class TransactionRepository:
    """Transaction repository"""

    def __init__(self, data: Transaction) -> None:
        self._data = data
        self._tax_limit = default_settings.TAX_LIMIT
        self._tax_percentage = default_settings.TAX_PERCENTAGE
        self._details = CalculationDetails()

    def _tax_calculation(
        self,
        item: TransactionItem,
        total: Decimal,
    ) -> Decimal:
        """Method responsible for calculating the tax of the unit operation.
        Args:
            item (TransactionItem): transaction item instance
            total (Decimal): total operation value
        Returns:
            Decimal: returns the tax amount
        """
        result = 0
        if (
            total > self._tax_limit
            and item.unit_cost > self._details.average_price
            and self._details.profit > 0
        ):
            result = self._details.profit * (self._tax_percentage / 100)
        return round(result, 2)

    def _calculate_average_price(
        self,
        item: TransactionItem,
        total: Decimal,
    ) -> None:
        """Method responsible for calculating the weighted average.
        Args:
            item (TransactionItem): transaction item instance
            total (Decimal): total operation value
        """
        total_investment = self._details.acquired_investment + item.quantity
        average_ratio = (
            self._details.acquired_investment * self._details.average_price
        )

        new_average = (average_ratio + total) / total_investment
        self._details.average_price = round(new_average, 2)
        self._details.acquired_investment += item.quantity

    def _calculate_profit(self, item: TransactionItem) -> None:
        """Method responsible for calculating the profit obtained from the sale.
        Args:
            item (TransactionItem): transaction item instance
        """
        old_profit = self._details.profit if self._details.profit < 0 else 0

        self._details.profit = (
            (item.unit_cost - self._details.average_price) * item.quantity
        ) + old_profit

    def get_taxes(self) -> List[Any]:
        """Method responsible for generating and sending the results with tax
        values from the operations submitted for calculation.
        Returns:
            List[Any]: returns an array with the results.
        """
        results = Results()
        for item in self._data.__root__:
            total_operation = item.quantity * item.unit_cost
            match item.operation:
                case TypeOperation.buy.name:
                    self._details.purchased_price = item.unit_cost
                    self._calculate_average_price(item, total_operation)
                case TypeOperation.sell.name:
                    self._details.acquired_investment -= item.quantity
                    self._calculate_profit(item)
            result = ResultItem(
                tax=self._tax_calculation(item, total_operation)
            )
            results.__root__.append(result)

        return results.dict()["__root__"]
