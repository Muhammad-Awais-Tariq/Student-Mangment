import streamlit as st

if "is_student" not in st.session_state or not st.session_state.is_student:
    st.error("Access denied")
    st.stop()

st.success(f"You have signed in as {st.session_state.name}")
st.title("Student page")

options = ["My Grades" , "My GPA" , "My Stats ","My Rank" , "My Courses"]

option = st.selectbox("Select required functionality", options)

if st.button("Start"):
    if option == "My Grades":
        st.write("My Grades")
    elif option == "My GPA":
        st.write("My GPA")
    elif option == "My Stats":
        st.write("My Stats")
    elif option == "My Rank":
        st.write("My Rank")
    else:
        st.write("My Courses")