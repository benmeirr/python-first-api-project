import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [10, 12, 14, 16, 18],
    'marketing': [15, 18, 20, 22, 25],
    'development': [20, 22, 25, 28, 30],
}

df = pd.DataFrame(data)

multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["sales"],
                             max_selections=3)
st.write(multiselect)

st.divider()

slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

st.divider()

text_input = st.text_input("What's your name?", placeholder="John Doe")
st.write(f"Wellcome {text_input}")

st.divider()

num_input = st.number_input("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(num_input)

st.divider()

txt_area = st.text_area("Write a comment", height=500, placeholder="Write your comment here")
st.write(txt_area)




