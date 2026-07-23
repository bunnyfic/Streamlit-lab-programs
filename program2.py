'''
Write a Streamlit application to take 
user inputs for Student Name, Marks (0–100), 
and Subject (using a dropdown).
When the user clicks the "Calculate Grade" button,
display a success card showing the student details, 
percentage, and their final letter grade based on the score.
'''
import streamlit as st
st.title('STUDENT GRADE CALCULATOR')
name = st.text_input("Enter Student Name:")
marks = st.number_input("Enter Marks (0-100):", min_value=0, max_value=100, step=1)
subject = st.selectbox("Select Subject:", ["Math", "Science", "English", "History"])
if st.button("Calculate Grade"):
    # Calculate percentage
    percentage = (marks / 100) * 100

    # Determine letter grade
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    # Display success card
    st.success("Grade Calculated Successfully!")
    st.write(f"**Student Name:** {name}")
    st.write(f"**Subject:** {subject}")
    st.write(f"**Marks:** {marks}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Letter Grade:** {grade}")