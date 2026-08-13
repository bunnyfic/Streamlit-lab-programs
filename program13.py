'''
Create a streamlit application that includes multiple pages.
Page 1: Home page,
Page 2: Data upload,
Page 3: Visualisation applies
to a custom theme and allows user to interactively edit a dataframe
'''

import pandas as pd
import streamlit as st

# PAGE 1: HOME PAGE
def home_page():
    st.title("Home")
    st.write("Welcome to the Multi-Page Analytics Application.")
    st.info("Navigate through the pages using the page menu on the left.")

# PAGE 2: DATA UPLOAD
def upload_page():
    st.title("Data Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.session_state['df'] = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully")
        st.dataframe(st.session_state['df'].head())
    elif "df" in st.session_state:
        st.info("Current dataset stored in session:")
        st.dataframe(st.session_state['df'].head())


# PAGE 3: VISUALIZATION & DATA EDITOR
def viz_page():
    st.title("Visualization & Data Editor")

    # Load dataset from session state or use default
    if "df" in st.session_state:
        df = st.session_state["df"]
    else:
        st.info("No file uploaded yet. Using default sample data:")
        df = pd.DataFrame({
            "Category": ["Product A", "Product B", "Product C", "Product D"],
            "Sales": [100, 250, 150, 300],
        })

    # Interactive Dataframe Editor
    st.subheader("Interactive Data Editor")
    edited_df = st.data_editor(df, num_rows="dynamic")

    # Chart
    st.subheader("Dynamic Bar Chart")
    numeric_cols = edited_df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        st.bar_chart(edited_df[numeric_cols[0]])
    else:
        st.warning(
            "Please make sure your dataframe contains at least one numeric column."
        )


# PAGE ROUTING SETUP
p1 = st.Page(home_page, title="Home")
p2 = st.Page(upload_page, title="Data Upload")
p3 = st.Page(viz_page, title="Visualization")

# Run Streamlit Router
pg = st.navigation([p1, p2, p3])
pg.run()