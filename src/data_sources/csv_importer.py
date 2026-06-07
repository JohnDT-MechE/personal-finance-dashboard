from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["date", "description", "amount"]


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

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in transactions.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
            f"Required columns are: {REQUIRED_COLUMNS}"
        )
    
    transactions["date"] = pd.to_datetime(transactions["date"], errors="coerce")
    transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")
    transactions["description"] = transactions["description"].astype(str).str.strip()

    transactions = transactions.dropna(subset=["date", "amount"])

    if "category" not in transactions.columns:
        transactions["category"] = "Uncategorized"

    if "account" not in transactions.columns:
        transactions["account"] = "Unknown"
    
    transactions = transactions.sort_values("date", ascending=False)

    return transactions