# Personal Finance Dashboard

A personal finance dashboard built with Python, Pandas, Plotly, and Streamlit to help track spending, budgets, net worth, and financial trends.

## Overview

Managing personal finances often requires reviewing bank statements, tracking spending habits, monitoring budgets, and understanding changes in net worth over time. This project aims to provide a centralized dashboard that makes financial data easy to analyze and visualize.

The dashboard will allow users to import transaction data, categorize spending, compare expenses against budgets, track assets and liabilities, and view interactive visualizations of their financial activity.

## Features

### Current Goals

* Import transaction data from CSV files
* Categorize transactions automatically
* Track spending by category
* Create and monitor monthly budgets
* Track net worth over time
* Generate interactive financial visualizations

### Planned Future Enhancements

* Automatic bank account synchronization
* Investment portfolio tracking
* Savings goal monitoring
* Recurring expense detection
* Subscription tracking
* Financial forecasting and trend analysis

## Project Structure

```text
personal-finance-dashboard/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── categorizer.py
│   ├── transaction_schema.py
│   ├── budget.py
│   ├── networth.py
│   ├── visualizations.py
│   │
│   └── data_sources/
│       ├── __init__.py
│       ├── csv_importer.py
│       └── plaid_importer.py
│
├── app/
│   └── dashboard.py
│
├── tests/
│   ├── test_budget.py
│   └── test_categorizer.py
│
└── docs/
    └── screenshots/
    └── pdfs/
```

## Technologies

* Python
* Pandas
* Plotly
* Streamlit
* Pytest

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd personal-finance-dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Dashboard

Start the Streamlit application:

```bash
streamlit run app/dashboard.py
```

The dashboard will then be available in your web browser.

## Development Roadmap

### Phase 1: Data Import and Categorization

* CSV transaction import
* Data validation and cleaning
* Spending category assignment
* Initial dashboard layout

### Phase 2: Budget Tracking

* Monthly budget creation
* Budget vs. actual spending analysis
* Budget alerts and summaries

### Phase 3: Net Worth Tracking

* Asset tracking
* Liability tracking
* Net worth history and trends

### Phase 4: Visualization and Analytics

* Spending breakdown charts
* Monthly trend analysis
* Budget performance dashboards
* Net worth growth visualizations

### Phase 5: Financial Account Integration

* Plaid integration
* Automated transaction syncing
* Multi-account support
* Near real-time dashboard updates

## Testing

Run unit tests with:

```bash
pytest
```

## License

This project is intended for educational and personal use.

## Author

John Dominguez-Trujillo

Summer 2026 Python Project
