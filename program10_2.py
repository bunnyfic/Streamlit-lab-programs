'''
Design a streamlit layout with columns,tables and sidebars to display
different content such as text,image and charts.
'''
import streamlit as st
import pandas as pd

st.sidebar.title("Sidebar Controls")
option = st.sidebar.selectbox("Choose view:", ["Option A", "Option B"])

st.title("Simple Dashboard")
st.write(f"Currently viewing: **{option}**")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Table")
    df = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Score": [85, 90]
    })
    st.dataframe(df)

with col2:
    st.subheader("Image & Chart")
    st.image(r"C:\Users\mywin\OneDrive\Pictures\brainmri.jpg", caption="Sample Image")
    st.bar_chart([10, 20, 30])