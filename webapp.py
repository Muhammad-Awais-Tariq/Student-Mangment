import streamlit as st

st.set_page_config(page_title="Student App", layout="centered")

st.title("Student Management")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "is_sudent" not in st.session_state:
    st.session_state.is_student = False

name = st.text_input("Enter your name: ")
password = st.text_input("Enter your password: ", type="password")

students = {"awais" : "123" , "ali" : "123" , "ahmed" : "!23"}
if st.button("Submit"):
    if name == "Admin" and password == "123":
        st.session_state.is_admin = True
        st.switch_page("pages/adminpage.py")
    for k,v in students.items():
        if name == k and password == v:
            st.session_state.is_student = True
            st.switch_page("pages/students.py")            
    else:
        st.error("Login info not correct")