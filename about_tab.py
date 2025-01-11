import streamlit as st


class AboutTab:
    @staticmethod
    def show():
        # Project Overview
        st.header("Customer Churn Analysis Project")
        st.write("""
        This dashboard provides comprehensive analysis of customer churn patterns in the banking sector. 
        It helps identify key factors contributing to customer attrition and provides insights for retention strategies.
        """)

        # How to Use
        st.subheader("How to Use This Dashboard")
        st.write("""
        1. Use the sidebar filters to select specific customer segments
        2. Navigate through different tabs to explore various aspects of the analysis
        3. Interact with charts to get detailed information
        4. Export data and visualizations as needed
        """)