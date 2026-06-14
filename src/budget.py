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

def validate_budget_data(budgets: pd.DataFrame) -> None:
    """
    Validate that a budget DataFrame contains the required columns.
    """
    required_columns = {"category", "budget"}

    missing_columns = required_columns - set(budgets.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required budget columns: {sorted(missing_columns)}"
        )
    
    if budgets["category"].isna().any():
        raise ValueError("Budget categories cannot be empty.")
    
    if budgets["budget"].isna().any():
        raise ValueError("Budget amounts cannot be emoty.")
    
    if(budgets["budget"] < 0).any():
        raise ValueError("Budget amounts cannot be negative.")
    

def compare_spending_to_budget(
    transactions: pd.DataFrame,
    budgets: pd.DataFrame,
) -> pd.DataFrame:
    """
    Compare actual spending by category against budget limits.

    Returns columns:
    - category
    - budget
    - spent
    - remaining
    - percent_used
    - status
    """
    validate_budget_data(budgets)

    spending = summarize_spending_by_category(transactions).rename(
        columns={"amount": "spent"}
    )

    comparison = budgets.merge(
        spending,
        on="category",
        how="left",
    )

    comparison["spent"] = comparison["spent"].fillna(0.0)

    comparison["remaining"] = (
        comparison["budget"] - comparison["spent"]
    )

    comparison["percent_used"] = comparison.apply(
        lambda row: (
            row["spent"] / row["budget"] * 100
            if row["budget"] > 0
            else 0.0
        ),
        axis=1,
    )

    comparison["status"] = comparison.apply(
        determine_budget_status,
        axis=1,
    )

    return comparison.sort_values(
        "percent_used",
        ascending=False,
    ).reset_index(drop=True)


def determine_budget_status(row: pd.Series) -> str:
    """
    Determine the status of a budget category.
    """
    if row["spent"] > row["budget"]:
        return "Over Budget"
    
    if row["percent_used"] >= 80:
        return "Near Limit"
    
    return "Within Budget"


def calculate_total_budget(budgets: pd.DataFrame) -> float:
    """
    Calculate the total amount budgeted.
    """
    validate_budget_data(budgets)

    return float(budgets["budget"].sum())


def calculate_total_budget_remaining(
    transactions: pd.DataFrame,
    budgets: pd.DataFrame,
) -> float:
    """
    Calculate total budget remaining across all categories.
    """
    comparison = compare_spending_to_budget(
        transactions,
        budgets,
    )

    return float(comparison["remaining"].sum())
