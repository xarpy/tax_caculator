from decimal import Decimal
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, validator


class TypeOperation(Enum):
    """Enum model for Operations type"""

    buy = 1
    sell = 2


class TransactionItem(BaseModel):
    """Transaction item model"""

    operation: str
    unit_cost: Decimal = Field(alias="unit-cost")
    quantity: int


class Transaction(BaseModel):
    """Transaction array model"""

    __root__: List[TransactionItem]


class ResultItem(BaseModel):
    """Result item model"""

    tax: Decimal

    @validator("tax", pre=False)
    def _format_field(cls, value):
        return value.to_eng_string()


class Results(BaseModel):
    """Results array model"""

    __root__: List[ResultItem] = []


class CalculationDetails(BaseModel):
    """Calculation details model"""

    profit: Decimal = 0
    purchased_price: Decimal = 0
    average_price: Decimal = 0
    acquired_investment: int = 0
