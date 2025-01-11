import numpy as np
import streamlit as st


class ClassifierTab:
    @staticmethod
    def show():
        # Page Title
        st.title("Manual Data Entry for Classification")

        # Create two columns
        col1, col2 = st.columns(2)

        # Column 1 Inputs
        with col1:
            row_number = st.number_input("RowNumber", min_value=1, value=1, step=1)
            customer_id = st.number_input("CustomerId", min_value=1, value=123456, step=1)
            surname = st.text_input("Surname", value="Smith")
            credit_score = st.number_input("CreditScore", min_value=0, max_value=1000, value=650, step=1)
            geography = st.selectbox("Geography", ["France", "Germany", "Spain"], index=0)
            gender = st.selectbox("Gender", ["Male", "Female"], index=0)

        # Column 2 Inputs
        with col2:
            age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
            tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5, step=1)
            balance = st.number_input("Balance", min_value=0.0, value=10000.0, step=100.0)
            num_of_products = st.number_input("NumOfProducts", min_value=1, max_value=4, value=2, step=1)
            has_cr_card = st.selectbox("HasCrCard", [True, False], index=0)
            is_active_member = st.selectbox("IsActiveMember", [True, False], index=0)
            estimated_salary = st.number_input("EstimatedSalary", min_value=0.0, value=50000.0, step=100.0)

        # Classify Button
        if st.button("Classify"):
            # Prepare the input data for prediction
            input_data = np.array([[
                credit_score,
                1 if geography == "France" else 2 if geography == "Germany" else 3,  # Encode geography
                1 if gender == "Male" else 0,  # Encode gender
                age,
                tenure,
                balance,
                num_of_products,
                1 if has_cr_card else 0,  # Encode HasCrCard
                1 if is_active_member else 0,  # Encode IsActiveMember
                estimated_salary
            ]])

            # is_exit = model.predict(input_data)
            is_exit = 0

            # Display the result
            st.metric("Classification Result", is_exit)

