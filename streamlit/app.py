import pandas as pd
import streamlit as st

df = pd.read_csv('./data/Iris/Iris.csv')
st.dataframe(df)

length_iris = df[['sepal_length', 'petal_length']]

st.write('Extracted lengths:')
st.dataframe(length_iris)


