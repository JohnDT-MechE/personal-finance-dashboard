import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_category_spending_bar_chart(category_summary: pd.DataFrame) -> go.Figure:
    """
    Create a bar chart showing spending by category.
    Expects a DataFrame with columns:
    - category
    - amount
    """
    fig = px.bar(
        category_summary,
        x="category",
        y="amount",
        title="Spending by Category",
        labels={
            "category": "Category",
            "amount": "Amount Spent ($)",
        },
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Amount Spent ($)",
        showlegend=False,
    )

    return fig


def create_category_spending_pie_chart(category_summary: pd.DataFrame) -> go.Figure:
    """
    Create a pie chart showing spending distribution by category.
    Expects a DataFrame with columns:
    - category
    - amount
    """
    fig = px.pie(
        category_summary,
        names="category",
        values="amount",
        title="Spending Distribution",
        hole=0.35,
    )

    return fig


def create_monthly_spending_line_chart(monthly_summary: pd.DataFrame) -> go.Figure:
    """
    Create a line chart showing spending over time.
    Expects a DataFrame with columns:
    - month
    - amount
    """
    fig = px.line(
        monthly_summary,
        x="month",
        y="amount",
        markers=True,
        title="Monthly Spending Trend",
        labels={
            "month": "Month",
            "amount": "Amount Spent ($)",
        },
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Amount Spent ($)",
    )

    return fig
