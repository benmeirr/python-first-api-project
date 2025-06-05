import streamlit as st
import pandas as pd


data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [10, 12, 14, 16, 18],
    'marketing': [15, 18, 20, 22, 25],
    'development': [20, 22, 25, 28, 30],
}

df = pd.DataFrame(data)

st.write(df)

st.line_chart(df, x="year", y=["sales", "marketing", "development"])

st.area_chart(df, x="year", y=["sales", "marketing"])

st.bar_chart(df, x="year", y=["sales", "marketing", "development"])