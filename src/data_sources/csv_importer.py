from pathlib import Path

import pandas as pd

from src.transaction_schema import (
    DEFAULT_TRANSACTION_VALUES,
    TRANSACTION_COLUMNS,
    validate_transaction_columns,
)


def load_transactions_csv(file_path: str | Path) -> pd.DataFrame:
    """
    Load transactions from a CSV file and standardize the data.

    Expected columns:
    - date
    - description
    - amount

    Optional columns:
    - category
    - account
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    transactions = pd.read_csv(file_path)

    transactions.columns = (
        transactions.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    validate_transaction_columns(list(transactions.columns))
    
    transactions["date"] = pd.to_datetime(transactions["date"], errors="coerce")
    transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")
    transactions["description"] = transactions["description"].astype(str).str.strip()

    transactions = transactions.dropna(subset=["date", "amount"])

    for column, default_value in DEFAULT_TRANSACTION_VALUES.items():
        if column not in transactions.columns:
            transactions[column] = default_value
    
    transactions = transactions[TRANSACTION_COLUMNS]
    transactions = transactions.sort_values("date", ascending=False)

    return transactions
