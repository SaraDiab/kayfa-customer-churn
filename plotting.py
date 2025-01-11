import pandas as pd
import plotly.express as px
import streamlit as st


class Plotting:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def scatter_plot(self, x: str, y: str,title: str):
        fig = px.scatter(
            self.data, x=x, y=y,
            color='Exited', title=title,
            color_discrete_map={0: "green", 1: "red"},
            labels={y: y.replace('_', ' ').title(), x: x.replace('_', ' ').title()}
        )
        st.plotly_chart(fig, use_container_width=True)

    def bar_chart(self, x: str, y: str,title: str):
        fig = px.bar(
            self.data, x=x, y=y, color='Gender',
            title=title,
            labels={y: y.replace('_', ' ').title(), x: x.replace('_', ' ').title()}
        )
        st.plotly_chart(fig, use_container_width=True)

    def pie_chart(self, names: str, values: str, title: str, hole: float = None):
        fig = px.pie(
            self.data, names=names, values=values,
            title=title, hole=hole,
            labels={values: values.replace('_', ' ').title(), names: names.replace('_', ' ').title()}
        )
        st.plotly_chart(fig, use_container_width=True)

