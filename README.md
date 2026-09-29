Student Management System

A Python-based Student Management System developed as a PBL/Micro Project for the subject Python for Data Science. The application allows users to add, search, update, delete, and analyze student records through an interactive web interface.

Project Description

The Student Management System is an interactive web application developed using Python, Pandas, Streamlit, and Matplotlib.

The system allows users to manually enter student details such as Student ID, Name, Gender, Age, Course, Semester, Email, Attendance, Marks, and Status.

Student records are stored in a CSV file. The application also provides search, update, delete, data analysis, and graphical visualization features.

Objectives
To develop a student management application using Python.
To add and manage student records.
To search student information using Student ID.
To update existing student records.
To delete student records.
To store data in a CSV file.
To analyze student marks and attendance using Pandas.
To visualize student data using Matplotlib.
To develop an interactive web application using Streamlit.
To implement Streamlit as a beyond-syllabus topic.
Features
Add Student
View Student Records
Search Student
Update Student
Delete Student
Duplicate Student ID Checking
CSV Data Storage
Student Data Analysis
Average Marks Analysis
Average Attendance Analysis
Highest and Lowest Marks
Active Student Count
Students by Course
Students by Status
Student Marks Graph
Marks Distribution Graph
Students by Course Graph
Attendance vs Marks Graph
Interactive Web Interface
Technologies Used
Python – Main programming language
Pandas – Data management and analysis
Streamlit – Interactive web application
Matplotlib – Data visualization
CSV – Student data storage
Beyond Syllabus Topic
Streamlit – Interactive Web Application Development

Streamlit is used as the beyond-syllabus topic in this project.

Streamlit is used to convert the Python program into an interactive web application. Users can perform operations such as adding, searching, updating, and deleting student records through the web interface.

The application also displays student analysis and graphical visualizations.

Student Information

The system stores the following student details:

Student ID
Student Name
Gender
Age
Course
Semester
Email
Attendance Percentage
Marks Percentage
Status
Main Operations
1. Add Student

Users can enter new student information and save it to the CSV file. The system also checks whether the Student ID already exists.

2. Search Student

Users can search for a student by entering the Student ID.

3. Update Student

Existing student information can be updated using the Student ID.

4. Delete Student

A student record can be deleted using the Student ID.

5. Analysis

The system provides:

Total Students
Average Marks
Average Attendance
Highest Marks
Lowest Marks
Active Students
Students by Course
Students by Status
6. Graph

The system provides different visualizations:

Student Marks
Marks Distribution
Students by Course
Attendance vs Marks
Data Storage

Student records are stored in:

student_management_system.csv

The CSV file is automatically created when it does not already exist.

Project Structure
Student-Management-System/
│
├── pds.py
├── student_management_system.csv
├── README.md
├── requirements.txt
└── screenshots/
Installation

Install the required libraries using:

pip install -r requirements.txt

The requirements.txt file contains:

streamlit
pandas
matplotlib
How to Run

Run the following command:

python -m streamlit run pds.py

The application will open in the browser at:

http://localhost:8501

Future Scope

The project can be extended by adding:

Login and User Authentication
Subject-wise Marks
Grade Calculation
Advanced Student Reports
Database Connectivity
Export Reports to PDF/Excel
Machine Learning-based Student Performance Prediction
Conclusion

The Student Management System demonstrates the practical application of Python for Data Science for managing and analyzing student data. It combines Pandas for data handling, Streamlit for web application development, Matplotlib for visualization, and CSV for data storage to create an interactive student management application.

Author

Name: Samarth Patel
Subject: Python for Data Science
Project: Student Management System
Project Type: PBL 3 – Micro Project
Beyond Syllabus: Streamlit – Interactive Web Application Development
