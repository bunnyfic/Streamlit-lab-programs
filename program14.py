'''
Build a Streamlit application that performs automated
analysis on uploaded data and generates a
downloadable report summarizing key statistics and visualisations.
'''

import pandas as pd
import streamlit as st

st.title("Simple Data Analyzer")

# 1. File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 2. Data Preview
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # 3. Summary Statistics
    st.subheader("Key Statistics")
    summary = df.describe().T
    st.dataframe(summary, use_container_width=True)

    # 4. Automated Visualization
    st.subheader("Column Distribution")
    num_cols = df.select_dtypes(include="number").columns

    if len(num_cols) > 0:
        selected_col = st.selectbox(
            "Select numerical column",
            num_cols
        )
        st.bar_chart(df[selected_col])
    else:
        st.warning("No numerical columns found to plot.")

    # 5. Report Download
    st.subheader("Export Summary Report")

    st.download_button(
        label="Download Statistics (.csv)",
        data=summary.to_csv(),
        file_name="data_summary.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to analyze.")