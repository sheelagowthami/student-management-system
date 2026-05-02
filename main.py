import streamlit as st
import os

FILE_NAME = "students.txt"

# -------------------------------
# FUNCTION: Calculate Grade
# -------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


# -------------------------------
# FUNCTION: Add Student
# -------------------------------
def add_student(name, age, marks):
    grade = calculate_grade(marks)

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{age},{marks},{grade}\n")

    return grade


# -------------------------------
# FUNCTION: Load Students
# -------------------------------
def load_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, age, marks, grade = line.strip().split(",")
                students.append([name, age, marks, grade])

    return students


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="Student Management System", layout="centered")

st.title("🎓 Student Management System")
st.write("A simple real-world dashboard using Python + Streamlit")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students", "Search Student"])


# -------------------------------
# ADD STUDENT
# -------------------------------
if menu == "Add Student":
    st.subheader("➕ Add New Student")

    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1, max_value=100)
    marks = st.number_input("Enter Marks (0-100)", min_value=0, max_value=100)

    if st.button("Add Student"):
        grade = add_student(name, age, marks)
        st.success(f"Student Added Successfully! Grade: {grade}")


# -------------------------------
# VIEW STUDENTS
# -------------------------------
elif menu == "View Students":
    st.subheader("📋 All Students")

    students = load_students()

    if students:
        st.table(students)
    else:
        st.warning("No student records found.")


# -------------------------------
# SEARCH STUDENT
# -------------------------------
elif menu == "Search Student":
    st.subheader("🔍 Search Student")

    search_name = st.text_input("Enter name to search")

    if st.button("Search"):
        students = load_students()
        found = False

        for s in students:
            if s[0].lower() == search_name.lower():
                st.success("Student Found!")
                st.write("Name:", s[0])
                st.write("Age:", s[1])
                st.write("Marks:", s[2])
                st.write("Grade:", s[3])
                found = True
                break

        if not found:
            st.error("Student not found")
