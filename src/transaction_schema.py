REQUIRED_TRANSACTION_COLUMNS = [
    "date",
    "description",
    "amount",
]

OPTIONAL_TRANSACTION_COLUMNS = [
    "category",
    "account",
]

TRANSACTION_COLUMNS = REQUIRED_TRANSACTION_COLUMNS + OPTIONAL_TRANSACTION_COLUMNS


DEFAULT_TRANSACTION_VALUES = {
    "category": "Uncategorized",
    "account": "Unknown",
}


def validate_transaction_columns(columns: list[str]) -> None:
    """
    Validate that the required transaction columns are present.
    """
    missing_columns = [
        column for column in REQUIRED_TRANSACTION_COLUMNS
        if column not in columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required transaction columns: {missing_columns}"
            f"Required columns are: {REQUIRED_TRANSACTION_COLUMNS}"
        )
