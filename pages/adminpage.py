import streamlit as st
from main import insert_student
if "is_admin" not in st.session_state or not st.session_state.is_admin:
    st.error("Access denied")
    st.stop()

st.success(f"You have signed in as {st.session_state.name}")
st.title("Admin Page")

options = ["Enroll" , "Directory" , "Top Scores","Edit / Drop" , "Analytics "]

option = st.selectbox("Select required functionality", options)

if "is_selected" not in st.session_state:
    st.session_state.is_selected = False

if "last_option" not in st.session_state:
    st.session_state.last_option = None

if option != st.session_state.last_option:
    st.session_state.is_selected = False
    st.session_state.last_option = option

if st.button("Start"):
    st.session_state.is_selected = True
if st.session_state.is_selected:
    if option == "Enroll":
        id = st.text_input("Enter the Student id: ")
        name = st.text_input("Enter the Student name: ")
        password = st.number_input("Set password: ")
        program = st.selectbox("Select program" , ["BSCS","BSE","BBA","BSAI","BSEE"])
        semester = st.selectbox("Select semester" , [1,2,3,4,5,6,7,8])
        section =  st.selectbox("Select section" , ["A","B"])
        semesterGPA = st.number_input("Enter semester Gpa: ")
        cgpa = st.number_input("Enter cgpa: ")
        status = st.selectbox("Select status" , ["Active","Passive"])
        if st.button("INSERT"):
            insert_student(id,name,password,program,semester,section,semesterGPA,cgpa,status)
    elif option == "Directory":
        st.write("Directory")
    elif option == "Top Scores":
        st.write("Top Scores")
    elif option == "Edit / Drop":
        st.write("Edit / Drop")
    else:
        st.write("Analytics")