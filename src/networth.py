import pandas as pd

REQUIRED_NET_WORTH_COLUMNS = {
    "date",
    "account",
    "account_type",
    "balance",
}


ASSET_TYPES = {
    "Checking",
    "Savings",
    "Investment",
    "Retirement",
    "Property",
    "Other Asset",
}


LIABILITY_TYPES = {
    "Credit Card",
    "Student Loan",
    "Auto Loan",
    "Mortgage",
    "Personal Loan",
    "Other Liability",
}


def validate_net_worth_data(accounts: pd.DataFrame) -> None:
    """
    Validate the structure and values of net worth account data.
    """
    missing_columns = REQUIRED_NET_WORTH_COLUMNS - set(accounts.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required net worth columns: {sorted(missing_columns)}"
        )
    
    if accounts["date"].isna().any():
        raise ValueError("Net worth dates cannot be emoty.")
    
    if accounts["account"].isna().any():
        raise ValueError("Account names cannot be empty.")
    
    if accounts["account_type"].isna().any():
        raise ValueError("Account types cannot be empty.")
    
    if accounts["balance"].isna().any():
        raise ValueError("Account balances cannot be empty.")
    
    valid_account_types = ASSET_TYPES | LIABILITY_TYPES

    invalid_types = set(accounts["account_type"]) - valid_account_types

    if invalid_types:
        raise ValueError(
            f"Invalid account types: {sorted(invalid_types)}"
        )
    

def prepare_net_worth_data(accounts: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize net worth account data.
    """
    prepared = accounts.copy()

    prepared["date"] = pd.to_datetime(
        prepared["date"],
        errors="coerce",
    )

    prepared["account"] = (
        prepared["account"]
        .astype(str)
        .str.strip()
    )

    prepared["account_type"] = (
        prepared["account_type"]
        .astype(str)
        .str.strip()
    )

    prepared["balance"] = pd.to_numeric(
        prepared["balance"],
        errors="coerce",
    )

    validate_net_worth_data(prepared)

    return prepared


def calculate_total_assets(accounts: pd.DataFrame) -> float:
    """
    Calculate total assets using the most recent balance
    for each asset account.
    """
    prepared = prepare_net_worth_data(accounts)

    latest_accounts = get_latest_account_balances(prepared)

    assets = latest_accounts[
        latest_accounts["account_type"].isin(ASSET_TYPES)
    ]

    return float(assets["balance"].sum())


def calculate_total_liabilities(accounts: pd.DataFrame) -> float:
    """
    Calculate total liabilities using the most recent balance
    for each liability account.
    """
    prepared = prepare_net_worth_data(accounts)

    latest_accounts = get_latest_account_balances(prepared)

    liabilities = latest_accounts[
        latest_accounts["account_type"].isin(LIABILITY_TYPES)
    ]

    return float(liabilities["balance"].abs().sum())


def calculate_net_worth(accounts: pd.DataFrame) -> float:
    """
    Calculate current net worth.

    Net worth = total assets - total liabilities
    """
    total_assets = calculate_total_assets(accounts)
    total_liabilities = calculate_total_liabilities(accounts)

    return total_assets - total_liabilities


def get_latest_account_balances(
    accounts: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return the most recent entry for each account.
    """
    prepared = prepare_net_worth_data(accounts)

    latest = (
        prepared.sort_values("date")
        .groupby("account", as_index=False)
        .tail(1)
        .sort_values("account")
        .reset_index(drop=True)
    )

    return latest


def summarize_net_worth_history(
    accounts: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate assets, liabilities, and net worth for each date.
    """
    prepared = prepare_net_worth_data(accounts)

    history_rows = []

    for date, daily_accounts in prepared.groupby("date"):
        asset_total = daily_accounts.loc[
            daily_accounts["account_type"].isin(ASSET_TYPES),
            "balance",
        ].sum()

        liability_total = daily_accounts.loc[
            daily_accounts["account_type"].isin(LIABILITY_TYPES),
            "balance",
        ].abs().sum()

        history_rows.append(
            {
                "date": date,
                "assets": float(asset_total),
                "liabilities": float(liability_total),
                "net_worth": float(asset_total - liability_total),
            }
        )
    
    return (
        pd.DataFrame(history_rows)
        .sort_values("date")
        .reset_index(drop=True)
    )
