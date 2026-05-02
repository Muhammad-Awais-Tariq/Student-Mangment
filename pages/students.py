import streamlit as st
from main import show_courses,get_gpa , get_stat , get_rank , get_course_stats  
import pandas as pd

if "is_student" not in st.session_state or not st.session_state.is_student: #check to see if the student is logged in or not
    st.error("Access denied")
    st.stop()

st.success(f"You have signed in as {st.session_state.name}")
st.title("Student page")

if "is_selected" not in st.session_state:  #flag to prevent the delteion of field when streamlit rerun
    st.session_state.is_selected = False

if "last_option" not in st.session_state:  #to clear the fileds when the user select another option
    st.session_state.last_option = None

options = ["My Grades" , "My GPA" , "My Stats","My Rank" , "My Courses"]

option = st.selectbox("Select required functionality", options)

if option != st.session_state.last_option: #change flags when the user select another option
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
        st.progress(float(gpa["semesterGPA"]) / 4.0, text=f'{gpa["semesterGPA"]} / 4.0') #first part show the value the second part the text

        st.markdown("**Cumulative GPA Progress**")
        st.progress(float(gpa["cgpa"]) / 4.0, text=f'{gpa["cgpa"]} / 4.0')

    elif option == "My Stats":
        result = get_stat(st.session_state.name)

        st.markdown("## Academic Performance Summary")
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.success("Best Subject")
            st.markdown(f"**{result['MaxCourse'][0]['MaxCourseName']}**")  #it goes to the key of the result and it give courses in list so go the 0 and then find the max course
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
        rank = get_rank(st.session_state.name)

        st.markdown("## Academic Standing")
        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(label="Your Rank", value=f"# {rank['ranking']}")

        with col2:
            st.metric(label="Total Students", value=rank['total_student'])

        with col3:
            st.metric(label="Semester", value=rank['semester'])

        with col4:
            st.metric(label="Program", value=rank['program'])

        st.divider()

        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.info(f"You are ranked **{rank['ranking']}** out of **{rank['total_student']}** students in **{rank['program']}**, Semester **{rank['semester']}**")
    else:
        result = get_course_stats(st.session_state.name)

        st.markdown("## Enrolled Courses")
        st.divider()

        course_data = [
            {
                "Course Code": course["courseCode"],
                "Course Name": course["courseName"],
                "Instructor": course["instructor"],
                "Credit Hours": course["creditHours"],
            }
            for course in result["courses"]    #to loop throught the list of the courses
        ]

        course_data.append({ #appeneding the last row to show the sum of total credit hours
            "Course Code": "",
            "Course Name": "",
            "Instructor": "Total",
            "Credit Hours": result["sum"],   
        })

        st.table(course_data)