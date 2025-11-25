import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# another change

# OPEN/LOAD DATA
cvd = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

# st.dataframe(cvd.head())

x = st.slider('description')  # 👈 this is a widget

st.write(x, 'squared is', x * x)

iso_code = st.selectbox('these are iso codes', options=['NLD', 'CAN'])

st.write(iso_code)
# CLEAN/EXPLORE/MANIPULATE DATA




# SHOW FANCY VIZUALIZATIONS






'# Heading 1'


'## Heading 2'