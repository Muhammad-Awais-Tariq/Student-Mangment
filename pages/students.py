import streamlit as st
from main import show_courses,get_gpa , get_stat
import pandas as pd

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.success(f"You have signed in as {st.session_state.name}")
st.title("Student page")

if "is_selected" not in st.session_state:
    st.session_state.is_selected = False

if "last_option" not in st.session_state:
    st.session_state.last_option = None

options = ["My Grades" , "My GPA" , "My Stats","My Rank" , "My Courses"]

option = st.selectbox("Select required functionality", options)

if option != st.session_state.last_option:
    st.session_state.is_selected = False
    st.session_state.last_option = option

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
        gpa = get_gpa(st.session_state.name)

        st.markdown("### Academic Performance")
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Semester", value=gpa["semester"])

        with col2:
            st.metric(label="GPA", value=gpa["semesterGPA"])

        with col3:
            st.metric(label="CGPA", value=gpa["cgpa"])

        st.divider()

        st.markdown("**Semester GPA Progress**")
        st.progress(float(gpa["semesterGPA"]) / 4.0, text=f'{gpa["semesterGPA"]} / 4.0')

        st.markdown("**Cumulative GPA Progress**")
        st.progress(float(gpa["cgpa"]) / 4.0, text=f'{gpa["cgpa"]} / 4.0')

    elif option == "My Stats":
        result = get_stat(st.session_state.name)

        st.markdown("## Academic Performance Summary")
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.success("Best Subject")
            st.markdown(f"**{result['MaxCourse'][0]['MaxCourseName']}**")
            st.metric(label="Marks Obtained", value=result['MaxCourse'][0]['MaxObtainedMarks'])

        with col2:
            st.error("Weakest Subject")
            st.markdown(f"**{result['MinCourse'][0]['MinCourseName']}**")
            st.metric(label="Marks Obtained", value=result['MinCourse'][0]['MinObtainedMarks'])

        st.divider()

        col3, col4, col5 = st.columns([1, 2, 1])
        with col4:
            st.info("Overall Average")
            st.metric(label="Average Marks", value=f"{result['AvgCourse'][0]['average']:.2f}")      

    elif option == "My Rank":
        st.write("My Rank")
    else:
        st.write("My Courses")