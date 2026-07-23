'''
Create a Streamlit app that allows users to upload a CSV file.
If the file is uploaded successfully, present a st.multiselect() widget
in the sidebar allowing the user to select which specific columns they want to view.
Display only the selected columns in a tabular format using st.dataframe().
'''

import pandas as pd
import streamlit as st

st.title("column selector")
uploaded_file = st.file_uploader("upload a csv file", type=["csv"])
if uploaded_file is not None: 
    df = pd.read_csv(uploaded_file)
    st.success("file uploaded successfully")

    columns = st.multiselect("select columns to display", options=df.columns, default=list(df.columns))
    if columns:
        st.dataframe(df[columns])
    else :
        st.warning("please select at least one column to display")
else :
    st.info("please upload a csv file to display the contents")