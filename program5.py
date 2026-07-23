'''
create a streamlit app that allows users to 
upload a CSV file using st.file_uploader() 
and display the contents of the file in a table format using st.dataframe() or st.write()
'''
import pandas as pd
import streamlit as st
file = st.file_uploader("upload a csv file", type=["csv"])
if file is not None:
    st.success("file upload successfully")
    df = pd.read_csv(file)
    st.header("displaying dataframe using st.dataframe()")
    st.dataframe(df,use_container_width=True)
    st.header("displaying dataframe using st.write()")
    st.write(df)
    st.markdown("---")
    st.subheader("data summary (From uploaded file)")
    st.write(df.describe())
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv", "text/csv")
else :
    st.info("please upload a csv file to display the contents")