from pathlib import Path

import pandas as pd

from src.data_sources.csv_importer import load_transactions_csv


def load_transactions(file_path: str | Path) -> pd.DataFrame:
    """
    Load transactions from the selected data source.
    Currently supports CSV files.
    """
    return load_transactions_csv(file_path)