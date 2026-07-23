'''
Design a streamlit dashboard using st.columns()
to arrange multiple sections side by side , 
displaying different metrics such as a pie 
chart , bar graph , and a data summary.
'''

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Metrics Dashboard",layout="wide")
st.title("EMPLOYEE METRICS DASHBOARD")

df = pd.DataFrame({
"ename": ["John", "Alice", "Bob", "Eve", "Charlie","karina","leo"],
"age": [28, 34, 25, 30, 29, 26,27],
"department": ["HR", "Finance", "IT", "Marketing", "Sales", "IT","Finance"],
"BasicSalary": [50000, 60000, 55000, 70000, 65000, 58000,80000],
"netSalary": [45000, 54000, 49500, 63000, 58500, 52200,72000],
"PerformanceScore": [85, 90, 80, 95, 88, 92, 87],
})

st.subheader("Employee Data Summary")
st.dataframe(df,use_container_width=True)
st.header("key employee metrics at a glance")
col1,col2,col3=st.columns(3)
with col1:
    st.subheader("Net salary Distribution")
    fig,ax=plt.subplots()
    ax.pie(df["netSalary"],labels=df["ename"],autopct="%1.1f%%",startangle=90)
    st.pyplot(fig)

with col2:
    st.subheader("individual net salary")
    st.bar_chart(df.set_index("ename")["netSalary"])

with col3:
    st.subheader("Data Summary")
    st.write(df.describe())
st.markdown("---")
st.caption("optional : you can enhance this dashboard by" \
"adding filters,interactivity or additional metrics based on your requirements")

