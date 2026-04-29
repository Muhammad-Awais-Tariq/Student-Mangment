import streamlit as st

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.success(f"you have signed in as {st.session_state.name}")
st.title("Student page")

options = ["My Grades" , "My GPA" , "My Stats ","My Rank" , "My Courses"]

option = st.selectbox("Select required functionality", options)