import pandas as pd


CATEGORY_RULES = {
    "Groceries": [
        "smiths",
        "trader joe",
        "whole foods",
        "grocery",
    ],
    
    "General": [
        "walmart",
        "target",
        "costco",
    ],

    "Dining": [
        "chipotle",
        "mcdonald",
        "starbucks",
        "restaurant",
        "cafe",
        "pizza",
        "taco",
    ],

    "Gas": [
        "gas",
        "shell",
        "chevron",
        "exxon",
    ],

    "Transportation": [
        "uber",
        "lyft"
    ],

    "Subscriptions": [
        "netflix",
        "spotify",
        "hulu",
        "disney",
        "peacock",
        "apple",
        "youtube",
        "google",
    ],

    "Income": [
        "paycheck",
        "payroll",
        "deposit",
    ],
}


def categorize_transaction(description: str) -> str:
    """
    Suggest a category based on keywords in the transaction description.
    """

    description = str(description).lower()

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in description:
                return category
    
    return "Uncategorized"


def categorize_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Add a suggested category column without overwriting
    existing user-defined categories.
    """

    categorized = transactions.copy()

    categorized["suggested_category"] = categorized["description"].apply(
        categorize_transaction
    )

    if "category" not in categorized.columns:
        categorized["category"] = categorized["suggested_category"]
    
    return categorized
