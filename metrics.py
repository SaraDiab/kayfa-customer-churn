import pandas as pd
import streamlit as st


class MetricsDisplay:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.churn_rate = (df["Exited"].mean() * 100)
        self.avg_balance_churned = df[df["Exited"] == 1]["Balance"].mean()
        self.avg_balance_retained = df[df["Exited"] == 0]["Balance"].mean()
        self.avg_estimated_salary_churned = df[df["Exited"] == 1]["EstimatedSalary"].mean()
        self.avg_estimated_salary_retained = df[df["Exited"] == 0]["EstimatedSalary"].mean()

    def display_metrics(self):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(
            label="Overall Churn Rate",
            value=f"{self.churn_rate:.1f}%"
        )

        col2.metric(
            label="Avg Balance (Churned)",
            value=f"${self.avg_balance_churned:,.2f}",
            delta=f"${self.avg_balance_churned - self.avg_balance_retained:,.2f} vs Retained"
        )

        col3.metric(
            label="Avg Estimated Salary (Churned)",
            value=f"{self.avg_estimated_salary_churned:.1f}",
            delta=f"{self.avg_estimated_salary_churned - self.avg_estimated_salary_retained:.1f} vs Retained"
        )

        col4.metric(
            label="Total Customers",
            value=f"{len(self.df):,}",
            delta=f"{len(self.df[self.df['Exited'] == 1]):,} Churned"
        )

