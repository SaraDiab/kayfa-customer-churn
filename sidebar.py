import streamlit as st

class SideBar:
    def __init__(self, df):
        self.df = df
        self.geography_filter = None
        self.gender_filter = None
        self.product_filter = None
        self.credit_score_range = None
        self.age_range = None
        self.filtered_data = None
        self._create_sidebar()

    def _create_sidebar(self):
        # Sidebar header
        # st.sidebar.header("Banking Customer Analysis")

        # Sidebar image
        st.sidebar.image("churn.jpg")

        # Sidebar Brief
        st.sidebar.text("This dashboard analyzes customer\nchurn patterns and behaviors.")

        # Default options
        geography_options = ["All"] + list(self.df['Geography'].unique())
        gender_options = ["All"] + list(self.df['Gender'].unique())
        product_options = ["All"] + list(self.df['NumOfProducts'].unique())

        # Sidebar - Filtering
        self.geography_filter = st.sidebar.selectbox("Select Geography", options=geography_options, index=0)
        self.gender_filter = st.sidebar.selectbox("Select Gender", options=gender_options, index=0)
        self.product_filter = st.sidebar.selectbox("Select Number of Products", options=product_options, index=0)

        # Range sliders
        self.credit_score_range = st.sidebar.slider(
            "Credit Score Range",
            min_value=int(self.df['CreditScore'].min()),
            max_value=int(self.df['CreditScore'].max()),
            value=(int(self.df['CreditScore'].min()), int(self.df['CreditScore'].max()))
        )

        self.age_range = st.sidebar.slider(
            "Age Range",
            min_value=int(self.df['Age'].min()),
            max_value=int(self.df['Age'].max()),
            value=(int(self.df['Age'].min()), int(self.df['Age'].max()))
        )

        # Filter data based on user selection
        self.filtered_data = self.df.copy()

        if self.geography_filter != "All":
            self.filtered_data = self.filtered_data[self.filtered_data['Geography'] == self.geography_filter]
        if self.gender_filter != "All":
            self.filtered_data = self.filtered_data[self.filtered_data['Gender'] == self.gender_filter]
        if self.product_filter != "All":
            self.filtered_data = self.filtered_data[self.filtered_data['NumOfProducts'] == self.product_filter]

        self.filtered_data = self.filtered_data[
            (self.filtered_data['CreditScore'].between(self.credit_score_range[0], self.credit_score_range[1])) &
            (self.filtered_data['Age'].between(self.age_range[0], self.age_range[1]))
            ]
