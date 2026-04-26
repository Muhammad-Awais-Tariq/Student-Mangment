import streamlit as st

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.title("Student page")