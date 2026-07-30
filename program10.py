'''
Design a streamlit layout with columns,tables and sidebars to display
different content such as text,image and charts.
'''
import streamlit as st
import pandas as pd
st.title("Streamlit Layout Example")
st.sidebar.header("Controls")
st.sidebar.write("Use the controls below to customize the layout and content.")
st.sidebar.text_input("Enter your name", "User")
st.sidebar.slider("Select a value", 0, 100, 50)
st.sidebar.selectbox("Choose a chart type", ["Line Chart", "Bar Chart", "Area Chart"])
col1, col2 = st.columns(2)
pd = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
st.dataframe(pd)
st.image(r"C:\Users\mywin\OneDrive\Pictures\brainmri.jpg", caption="Sample Image")
st.line_chart(pd)
st.bar_chart(pd)
st.area_chart(pd)
st.write("This is a sample layout demonstrating the use of columns, tables, sidebars, and various content types in Streamlit.")

