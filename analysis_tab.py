import streamlit as st

from plotting import Plotting


class AnalysisTab:
    def __init__(self, filtered_data):
        self.plotting = Plotting(filtered_data)
        self.filtered_data = filtered_data

    def show(self):
        st.title("Churn Analysis Dashboard")

        # Main section
        bar_col, pie_col, donut_col = st.columns((4, 3, 3))

        with bar_col:
            exited_count_by_geography = self.filtered_data.groupby('Geography')['Exited'].value_counts().unstack(fill_value=0)
            exited_count = exited_count_by_geography[1].sum()  # Total Exited count
            title = f"Balance by Geography (Exited Count: {exited_count})"

            self.plotting.bar_chart(
                x="Geography",
                y="Balance",
                title=title
            )

        with pie_col:
            self.plotting.pie_chart(
                names="Exited",
                values="CreditScore",
                title="Churn vs Credit Score"
            )

        with donut_col:
            self.plotting.pie_chart(
                names="Geography",
                values="Exited",
                title="Churn by Region",
                hole=0.3
            )

        st.subheader(f"Customer Analysis for {self.filtered_data['Geography'].iloc[0]} Region")
        self.plotting.scatter_plot(x="Age", y="Balance", title="Age vs Balance Distribution")

