import streamlit as st

if "is_admin" not in st.session_state or not st.session_state.is_admin:
    st.error("Access denied")
    st.stop()

st.success(f"you have signed in as {st.session_state.name}")
st.title("Admin Page")