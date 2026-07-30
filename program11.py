'''Design and implement a Streamlit application integrated with an SQLite databse that
allows users to:
1. Insert and display student records.
2. Run custom SQL queries.
3. Visualize student data using filters and different chart types
 (Bar, Line, Histogram, Pie).'''

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# 1. Database Setup
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade TEXT,
        score REAL
    )
""")

conn.commit()

st.title("Student Database App")

# Navigation
menu = st.sidebar.radio(
    "Navigation",
    ["Insert & View", "Run Query", "Visualize"]
)
# INSERT AND DISPLAY RECORDS

if menu == "Insert & View":

    st.subheader(" Add Student Record")

    with st.form("add_form", clear_on_submit=True):
        name = st.text_input("Name")
        age = st.number_input("Age", 15, 100, 20)
        grade = st.selectbox("Grade", ["A", "B", "C", "D", "F"])
        score = st.slider("Score", 0.0, 100.0, 75.0)

        if st.form_submit_button("Save"):
            cursor.execute(
                "INSERT INTO students (name, age, grade, score) VALUES (?, ?, ?, ?)",
                (name, age, grade, score)
            )
            conn.commit()
            st.success(f"Saved record for {name}!")

    st.subheader(" All Records")

    df = pd.read_sql_query("SELECT * FROM students", conn)
    st.dataframe(df, use_container_width=True)

# RUN CUSTOM SQL QUERIES

elif menu == "Run Query":
    st.subheader(" Custom SQL Terminal")
    query = st.text_area("SQL Query:", "SELECT * FROM students")
    if st.button("Run"):
        try:
            if query.strip().upper().startswith("SELECT"):
                result_df = pd.read_sql_query(query, conn)
                st.dataframe(result_df, use_container_width=True)
            else:
                cursor.execute(query)
                conn.commit()
                st.success("Query executed successfully!")

        except Exception as e:
            st.error(f"Error: {e}")
# INSERT AND DISPLAY RECORDS

# VISUALIZE STUDENT DATA

elif menu == "Visualize":

    st.subheader(" Data Visualizations")

    df = pd.read_sql_query("SELECT * FROM students", conn)

    if df.empty:
        st.warning("No data found, please add records first.")

    else:

        selected_grade = st.multiselect(
            "Filter by Grade:",
            df["grade"].unique(),
            default=df["grade"].unique()
        )

        filtered_df = df[df["grade"].isin(selected_grade)]

        # Chart Selector

        chart_type = st.selectbox(
            "Select Chart Type:",
            ["Bar", "Line", "Histogram", "Pie"]
        )

        if chart_type == "Bar":
            fig = px.bar(
                filtered_df,
                x="name",
                y="score",
                color="grade",
                title="Score by Student"
            )

        elif chart_type == "Line":
            fig = px.line(
                filtered_df,
                x="name",
                y="score",
                markers=True,
                title="Score Trend"
            )

        elif chart_type == "Histogram":
            fig = px.histogram(
                filtered_df,
                x="score",
                title="Score Distribution"
            )

        elif chart_type == "Pie":
            fig = px.pie(
                filtered_df,
                names="grade",
                title="Grade Ratio"
            )

        st.plotly_chart(fig, use_container_width=True)