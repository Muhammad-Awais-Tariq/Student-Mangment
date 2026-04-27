import streamlit as st

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.success(f"you have signed in as {st.session_state.name}")
st.title("Student page")