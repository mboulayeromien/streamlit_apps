import pandas as pd, streamlit as st
st.write("""
# My first streamlit app
hello *world*""")
df  = pd.read_csv('book1.csv')
st.line_chart(df)
# .streamlit/secrets.toml


host = "localhost"
port = 3306
database = "pets"
user = "merci@gmail.com"
password = "romienmerci"