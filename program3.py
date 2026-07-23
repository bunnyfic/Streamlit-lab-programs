'''
Develope a streamlit web app that generates a dataset
of 100 records with random values across three columns (column 1,column 2,column 3)
Display the rawdata in an interactive dataframe 
plot its trends using a line chart and visualize the average 
of each column using bar chart 
'''
import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Analysis Dashboard")

data = pd.DataFrame(np.random.randn(100,3),
columns = ['column 1','column 2','column 3'])

st.subheader("RANDOM DATA TABLE")
st.dataframe(data)

st.subheader('Summary Statistics')
st.line_chart(data)

st.subheader('category comparison')
st.bar_chart(data.mean())