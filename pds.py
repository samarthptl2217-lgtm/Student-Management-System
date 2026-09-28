import streamlit as st
import pandas as pd
import os

# Page Configuration
st.set_page_config(
    page_title="Student Management System",
    layout="wide"
)

st.title(" Student Performance Management System")
st.write("Enter student details manually and analyze their performance.")

# CSV file
FILE_NAME = "student_dataset.csv"

# Create CSV if it does not exist
columns = [
    "Student_ID",
    "Name",
    "Age",
    "Gender",
    "Attendance",
    "Study_Hours",
    "Assignment_Marks",
    "Internal_Marks",
    "Practical_Marks",
    "Final_Marks",
    "Total_Marks",
    "Average_Marks",
    "Result"
]

if not os.path.exists(FILE_NAME):
    pd.DataFrame(columns=columns).to_csv(FILE_NAME, index=False)

# Student Entry Form
st.header("Enter Student Details")

with st.form("student_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        student_id = st.text_input("Student ID")
        name = st.text_input("Student Name")
        age = st.number_input("Age", min_value=15, max_value=30, value=18)

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

        study_hours = st.number_input(
            "Study Hours per Day",
            min_value=0.0,
            max_value=24.0,
            value=2.0
        )

    with col3:
        assignment = st.number_input(
            "Assignment Marks",
            min_value=0.0,
            max_value=100.0,
            value=50.0
        )

        internal = st.number_input(
            "Internal Marks",
            min_value=0.0,
            max_value=100.0,
            value=50.0
        )

        practical = st.number_input(
            "Practical Marks",
            min_value=0.0,
            max_value=100.0,
            value=50.0
        )

    final_marks = st.number_input(
        "Final Exam Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    submit = st.form_submit_button("Add Student")

# Add Student
if submit:

    if student_id == "" or name == "":
        st.error("Please enter Student ID and Student Name.")

    else:

        # Calculate total and average
        total = (
            assignment
            + internal
            + practical
            + final_marks
        )

        average = total / 4

        # Result condition
        if average >= 50 and attendance >= 75:
            result = "Pass"
        else:
            result = "Fail"

        # Create student record
        new_student = pd.DataFrame([{
            "Student_ID": student_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Attendance": attendance,
            "Study_Hours": study_hours,
            "Assignment_Marks": assignment,
            "Internal_Marks": internal,
            "Practical_Marks": practical,
            "Final_Marks": final_marks,
            "Total_Marks": total,
            "Average_Marks": round(average, 2),
            "Result": result
        }])

        # Read existing data
        df = pd.read_csv(FILE_NAME)

        # Check duplicate Student ID
        if student_id in df["Student_ID"].astype(str).values:
            st.warning("Student ID already exists.")

        else:

            # Add new student
            df = pd.concat(
                [df, new_student],
                ignore_index=True
            )

            # Save CSV
            df.to_csv(FILE_NAME, index=False)

            st.success(
                f"Student {name} added successfully!"
            )

            st.info(
                f"Average Marks: {average:.2f} | Result: {result}"
            )

# Display Student Data
st.header("Student Records")

df = pd.read_csv(FILE_NAME)

if len(df) > 0:

    st.dataframe(
        df,
        use_container_width=True
    )

    # Statistics
    st.header("Student Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Students",
            len(df)
        )

    with col2:
        st.metric(
            "Average Marks",
            round(df["Average_Marks"].mean(), 2)
        )

    with col3:
        st.metric(
            "Passed",
            (df["Result"] == "Pass").sum()
        )

    with col4:
        st.metric(
            "Failed",
            (df["Result"] == "Fail").sum()
        )

    # Charts
    st.header("Performance Visualization")

    chart_data = df.set_index("Name")["Average_Marks"]

    st.bar_chart(chart_data)

else:

    st.info(
        "No student records available. "
        "Enter student details using the form above."
    )