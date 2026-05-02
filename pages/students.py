import streamlit as st
from main import show_courses
import pandas as pd

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.success(f"You have signed in as {st.session_state.name}")
st.title("Student page")

if "is_selected" not in st.session_state:
    st.session_state.is_selected = False



options = ["My Grades" , "My GPA" , "My Stats ","My Rank" , "My Courses"]

option = st.selectbox("Select required functionality", options)

if st.button("Start"):
    st.session_state.is_selected = True

if st.session_state.is_selected:
    if option == "My Grades":
        courses = show_courses(st.session_state.name)
        df = pd.DataFrame(courses).rename(columns= {
            0 : 'Course Name',
            1: 'Total',    
            2: 'Obtained',
            3: 'Grade'})
        st.table(df)

    elif option == "My GPA":
        st.write("My GPA")
    elif option == "My Stats":
        st.write("My Stats")
    elif option == "My Rank":
        st.write("My Rank")
    else:
        st.write("My Courses")