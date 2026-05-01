import streamlit as st
from main import get_students

st.set_page_config(page_title="Student App", layout="centered")

st.title("Student Management")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "is_sudent" not in st.session_state:
    st.session_state.is_student = False

st.session_state.name = st.text_input("Enter your name: ")
password = st.text_input("Enter your password: ", type="password")

if st.button("Submit"):
    if st.session_state.name == "Admin" and password == "123":
        st.session_state.is_admin = True
        st.switch_page("pages/adminpage.py")
    elif st.session_state.name != "Admin":
            if get_students(st.session_state.name , password):
                st.session_state.is_student = True
                st.switch_page("pages/students.py")            
    else:
        st.error("Login info not correct")