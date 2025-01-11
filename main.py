import pandas as pd
import streamlit as st

from churn_dashboard import ChurnDashboard


def main():
    # Set the page config
    st.set_page_config(
        page_title="Banking Churn Analysis",
        page_icon="images//logo.jpg",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items=None
    )

    # Load the data
    df = pd.read_csv("customer_churn.csv")
    # Run the dashboard
    dashboard = ChurnDashboard(df)
    dashboard.run()


if __name__ == "__main__":
    main()