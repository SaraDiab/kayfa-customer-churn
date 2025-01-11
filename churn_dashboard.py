import pandas as pd
import streamlit as st

from analysis_tab import AnalysisTab
from classifier_tab import ClassifierTab
from data_tab import DataTab
from metrics import MetricsDisplay
from sidebar import SideBar
from about_tab import AboutTab


class ChurnDashboard:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.sidebar = SideBar(df)
        self.metrics_display = MetricsDisplay(self.sidebar.filtered_data)
        self.about_tab = AboutTab()
        self.analysis_tab = AnalysisTab(self.sidebar.filtered_data)
        self.data_tab = DataTab(self.sidebar.filtered_data)
        self.classifier_tab = ClassifierTab()

    def run(self):
        # Display metrics
        self.metrics_display.display_metrics()

        # Create tabs
        about_tab, analysis_tab, data_tab, classifier_tab = st.tabs([
            "📋 About Project",
            "📊 Analysis Dashboard",
            "🔍 Data Exploration",
            "🤖 Classifier",
        ])

        # Fill each tab
        with about_tab:
            self.about_tab.show()

        with analysis_tab:
            self.analysis_tab.show()

        with data_tab:
            self.data_tab.show()

        with classifier_tab:
            self.classifier_tab.show()
