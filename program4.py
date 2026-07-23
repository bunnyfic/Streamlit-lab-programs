'''
Create a basic Streamlit app that uses st.title(), 
st.header(), and st.write() to display text content, 
and st.image() to display an image.
'''
import streamlit as st

st.title("Basic Streamlit App")

st.header("This is a header")

st.write("This is a paragraph.")

st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo")