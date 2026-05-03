import streamlit as st
from main import insert_student , directory
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
        if "student_courses" not in st.session_state:
            st.session_state.student_courses = []
        if "register_course" not in st.session_state:
            st.session_state.register_course = False

        id = st.text_input("Enter the Student id: ")
        name = st.text_input("Enter the Student name: ")
        password = st.number_input("Set password: ")
        program = st.selectbox("Select program" , ["BSCS","BSE","BBA","BSAI","BSEE"])
        semester = st.selectbox("Select semester" , [1,2,3,4,5,6,7,8])
        section =  st.selectbox("Select section" , ["A","B"])
        semesterGPA = st.number_input("Enter semester Gpa: " , min_value=0.0, max_value=4.0)
        cgpa = st.number_input("Enter cgpa: " , min_value=0.0, max_value=4.0)
        status = st.selectbox("Select status" , ["Active","Passive"])
        available_course = {
            "CS101"  : ["Programming Fundamentals",  "Dr. Ahmed",   3],
            "MTH101" : ["Calculus",                  "Sir Bilal",   3],
            "ENG101" : ["English Composition",        "Ms. Sana",    2],
            "DB201"  : ["Database Systems",           "Dr. Noman",   3],
            "DS201"  : ["Data Structures",            "Dr. Fatima",  3],
            "SE201"  : ["Software Engineering",       "Sir Haris",   3],
            "AI301"  : ["Artificial Intelligence",    "Dr. Saad",    3],
            "CN301"  : ["Computer Networks",          "Sir Hamza",   3],
            "OS301"  : ["Operating Systems",          "Dr. Ayesha",  3],
            "SE101"  : ["Intro to SE",                "Sir Umar",    3],
            "ICT101" : ["ICT",                        "Ms. Hina",    2],
            "REQ201" : ["Requirements Engineering",   "Dr. Waqar",   3],
            "SQA201" : ["Software Quality",           "Sir Danish",  3],
            "PM301"  : ["Project Management",         "Dr. Salman",  3],
            "SAD301" : ["System Analysis",            "Sir Owais",   3],
            "WEB301" : ["Web Engineering",            "Ms. Aiman",   3],
            "FYP401" : ["Final Year Project",         "Dr. Irfan",   3],
            "ENT401" : ["Entrepreneurship",           "Sir Adnan",   2],
            "ACC101" : ["Accounting",                 "Sir Farhan",  3],
            "ECO101" : ["Economics",                  "Dr. Huma",    3],
            "MKT201" : ["Marketing",                  "Ms. Rabia",   3],
            "FIN201" : ["Finance",                    "Dr. Rizwan",  3],
            "HR301"  : ["Human Resource",             "Sir Jawad",   3],
            "MGT301" : ["Management",                 "Dr. Saba",    3],
            "STR401" : ["Strategic Management",       "Dr. Kamran",  3],
            "AI101"  : ["Intro to AI",                "Dr. Saad",    3],
            "ML201"  : ["Machine Learning",           "Dr. Ayesha",  3],
            "DL301"  : ["Deep Learning",              "Dr. Hassan",  3],
            "CV401"  : ["Computer Vision",            "Dr. Nida",    3],
            "CS201"  : ["Data Structures",            "Dr. Imran",   3],
            "MTH201" : ["Linear Algebra",             "Dr. Asif",    3],
            "CS401"  : ["Software Engineering",       "Dr. Ahsan",   3],
            "CS402"  : ["Operating Systems",          "Dr. Kashif",  3],
            "EE101"  : ["Circuits",                   "Dr. Mushtaq", 3],
            "EE201"  : ["Signals",                    "Dr. Mushtaq", 3],
            "EE401"  : ["Power Electronics",          "Dr. Pervaiz", 3],
            "BBA101" : ["Management",                 "Dr. Shahid",  3],
            "BBA201" : ["Macroeconomics",             "Dr. Farhan",  3],
            "BBA401" : ["Strategic Management",       "Dr. Shahid",  3],
        }
        if st.button("Register Course"):
            st.session_state.register_course = True

        if st.session_state.register_course:
            course = st.selectbox("Select course" , available_course.keys())
            subject = available_course[course][0]
            teacher = available_course[course][1]
            credit_hour = available_course[course][2]
            st.text_input("Subject",      value=subject,          disabled=True)
            st.text_input("Teacher",      value=teacher,          disabled=True)
            st.text_input("Credit Hours", value=str(credit_hour), disabled=True)
            if st.button("Add course"):
                st.session_state.student_courses.append({"courseCode" :course, "courseName" : subject, "instructor" : teacher, \
                                                         "creditHours" : credit_hour,"marksObtained" :0, "totalMarks" : 100,"grade" :None})
                st.session_state.register_course = False
                st.session_state.course_added = True
                st.rerun()
        if st.session_state.get("course_added"):
            st.success("Course added successfully!")
            st.session_state.course_added = False
        if st.button("INSERT"):
            insert_student(id,name,password,program,semester,section,semesterGPA,cgpa,status,st.session_state.student_courses)
            st.session_state.is_selected = False
            st.session_state.student_courses = []
            st.session_state.student_inserted = True
            st.rerun()
    elif option == "Directory":
        result = directory()

        st.markdown("## Directory")
        st.divider()

        course_data = [
            {
                "ID": student.get("studentId", "N/A"),
                "Name": student.get("fullName", "N/A"),
                "Semester": student.get("semester", "N/A"),
                "Section": student.get("section", "N/A"),
                "CGPA": student.get("cgpa", "N/A"),
                "Status": student.get("status", "N/A")
            }
            for student in result    
        ]

        st.dataframe(course_data)
    elif option == "Top Scores":
        st.write("Top Scores")
    elif option == "Edit / Drop":
        st.write("Edit / Drop")
    else:
        st.write("Analytics")

if st.session_state.get("student_inserted"):
        st.success("Student enrolled successfully!")
        st.session_state.student_inserted = False