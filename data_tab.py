import streamlit as st


class DataTab:
    def __init__(self, filtered_data):
        self.filtered_data = filtered_data

    def show(self):
        st.title("Data Exploration")

        # Data Overview
        st.header("Dataset Overview")
        st.write("Total Records:", len(self.filtered_data))

        # Summary Statistics
        st.subheader("Summary Statistics")
        st.write(self.filtered_data.describe())

        # Column Information
        st.subheader("Column Descriptions")
        col_descriptions = {
            'CustomerId': 'Unique identifier for each customer',
            'CreditScore': 'Credit score of the customer',
            'Geography': 'Customer\'s location',
            'Gender': 'Customer\'s gender',
            'Age': 'Customer\'s age',
            'Tenure': 'Number of years as a customer',
            'Balance': 'Account balance',
            'NumOfProducts': 'Number of bank products used',
            'HasCrCard': 'Whether the customer has a credit card',
            'IsActiveMember': 'Active membership status',
            'EstimatedSalary': 'Estimated salary of the customer',
            'Exited': 'Whether the customer has churned'
        }

        for col, desc in col_descriptions.items():
            st.text(f"{col}: {desc}")

        # Raw Data Table
        st.subheader("Raw Data")
        st.dataframe(self.filtered_data)

        # Export Option
        if st.button("Export Filtered Data to CSV"):
            csv = self.filtered_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="filtered_churn_data.csv",
                mime="text/csv"
            )
