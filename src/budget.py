import pandas as pd

def get_expenses(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Return only expense transactions.
    Expenses are transactions with negative amounts.
    """
    return transactions[transactions["amount"] < 0].copy()

def get_income(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Return only income transactions.
    Income transactions have positive amounts.
    """
    return transactions[transactions["amount"] > 0].copy()

def calculate_total_spending(transactions: pd.DataFrame) -> float:
    """
    Calculate total spending as a positive number.
    """
    expenses = get_expenses(transactions)
    return abs(expenses["amount"].sum())

def calculate_total_income(transactions: pd.DataFrame) -> float:
    """
    Calculate total income.
    """
    income = get_income(transactions)
    return income["amount"].sum()


def summarize_spending_by_category(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize spending by category.
    """
    expenses = get_expenses(transactions)

    summary = (
        expenses.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount")
    )

    summary["amount"] = summary["amount"].abs()

    return summary.sort_values("amount", ascending=False)

def summarize_monthly_spending(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize total spending by month.
    """
    expenses = get_expenses(transactions).copy()

    expenses["month"] = expenses["date"].dt.to_period("M").astype(str)

    summary = (
        expenses.groupby("month", as_index=False)["amount"]
        .sum()
        .sort_values("month")
    )

    summary["amount"] = summary["amount"].abs()

    return summary
