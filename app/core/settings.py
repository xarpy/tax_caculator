import os
from decimal import Decimal
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Project configuration class"""

    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    PROJECT_NAME: str = "TAX CALCULATOR"
    DESCRIPTION: str = "System based programming challenge"
    VERSION: str = "1.0.0"
    TAX_LIMIT: Decimal = os.getenv("TAX_LIMIT")
    TAX_PERCENTAGE: Decimal = os.getenv("TAX_PERCENTAGE")

    class Config:
        case_sensitive = True


default_settings = Settings()
