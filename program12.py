'''3  Create a Streamlit application that allows a chart
   (bar chart) and allows the user to filter
   data using slider and display table
   based on the selected range'''

import pandas as pd
import streamlit as st

# Title
st.title("Simple Data Filter App")

# Sample dataset
data = pd.DataFrame({
    'Category': ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F'],
    'Value': [12, 28, 45, 67, 85, 99]
})

# Range slider to select min and max values
min_val = int(data['Value'].min())
max_val = int(data['Value'].max())

selected_range = st.slider(
    "Select Value Range",
    min_value=min_val,
    max_value=max_val,
    value = (min_val,max_val),
)
# Filter the dataframe based on the slider selection
filtered_df = data[
    (data['Value'] >= selected_range[0]) & (data['Value'] <= selected_range[1])
]

# Display Bar Chart
st.subheader("Value by Category")
st.bar_chart(filtered_df.set_index('Category'))

# Display Data Table
st.subheader("Filtered Data")
st.dataframe(filtered_df)


