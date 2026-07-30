'''
Create a basic Streamlit app that demonstrates the
 use of widgets (buttons, sliders, text Input),
different layouts (columns or sidebar), 
and components to build an Interactive Interface
'''
import streamlit as st
st.sidebar.header("Controls")
user_name = st.sidebar.text_input("Enter your name","Developer")
item_count = st.sidebar.slider("Select number of items", 1, 10, 5)
st.title(f"Hello, {user_name}!")

col1,col2 = st.columns(2)
with col1:
    st.write(f"selected quantity:**{item_count}**")

with col2:
    if st.button("Click Me!"):
        st.success("Button clicked!")
