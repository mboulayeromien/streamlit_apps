import pandas as pd, streamlit as st, numpy as np
st.write("""
# My first streamlit app
hello *world*""")
df  = pd.read_csv('book1.csv')
st.line_chart(df)
