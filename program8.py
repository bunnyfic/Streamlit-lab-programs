'''Build a Streamlit app that lets a user upload a CSV file.
The app should automatically identify all numeric columns and
allow the user to select one numeric column from a dropdown
(st.selectbox()). Then, provide a slider (st.slider()) ranging
from the column's minimum value to its maximum value, filtering
the table to show only rows where that column's value
is greater than or equal to the selected slider value.'''