import streamlit as st

def main():
    st.set_page_config(
        page_title="Personal Finance Dashboard",
        page_icon="💰",
        layout="wide"
    )

    st.title("Personal Finance Dashboard")

    st.markdown(
        """
        Track spending, budgets, net worth, and financial trends from one dashboard.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Monthly Spending", "$0.00")

    with col2:
        st.metric("Budget Remaining", "$0.00")
    
    with col3:
        st.metric("Net Worth", "$0.00")

    st.divider()

    st.subheader("Dashboard Sections")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Transactions", "Soending", "Budgets", "Net Worth"]
    )

    with tab1:
        st.info("CSV transaction import will go here.")
    
    with tab2:
        st.info("Spending summaries and category charts will go here.")

    with tab3:
        st.info("Budget tracking will go here.")

    with tab4:
        st.info("Net worth tracking will go here.")

if __name__ == "__main__":
    main()