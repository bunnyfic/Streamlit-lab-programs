'''write a streamlit application to take
user inputs for name,age and role (using drop down), 
and display a formatted success card showing 
the generated profile when a submit button is clicked '''

import streamlit as st
st.title("User Profile Generator")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
role = st.selectbox("Select your role:", ["Developer", "Designer", "Manager", "Tester"])
if st.button("Submit"):
    st.success(f"Profile Created Successfully!")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Role:** {role}")

    st.markdown(
            f"""
            <div style="
                background-color:lightgreen;
                padding:20px;
                border-radius:10px;
                border-left:6px solid #28a745;
                margin-top:15px;
            ">
                <h3 style="color:#155724;">👤 User Profile</h3>
                <p><b>Name:</b> {name}</p>
                <p><b>Age:</b> {age}</p>
                <p><b>Role:</b> {role}</p>
            </div>
            """,
            unsafe_allow_html=True
        )