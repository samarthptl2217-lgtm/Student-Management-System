# Student Performance Management System

A Python-based **Student Performance Management System** developed as a PBL/Micro Project for the subject **Python for Data Science**. The application allows users to enter, manage, and analyze student performance data.

## Project Description

The Student Performance Management System is an interactive web application developed using **Python, Pandas, and Streamlit**.

Users can manually enter student details such as Student ID, Name, Attendance, Study Hours, Assignment Marks, Internal Marks, Practical Marks, and Final Exam Marks.

The system automatically calculates the total and average marks and determines the student's Pass/Fail result.

## Objectives

* To develop a student management application using Python.
* To manually enter and manage student records.
* To calculate total and average marks automatically.
* To determine student Pass/Fail results.
* To store student records in a CSV file.
* To analyze student performance using Pandas.
* To display student statistics and visualization.
* To implement Streamlit as a beyond-syllabus topic.

## Features

* Add Student
* View Student Records
* Remove Student
* Duplicate Student ID Checking
* Automatic Total Marks Calculation
* Automatic Average Marks Calculation
* Pass/Fail Result
* CSV Data Storage
* Student Statistics
* Performance Visualization
* Interactive Web Interface

## Technologies Used

* **Python** – Main programming language
* **Pandas** – Data management and analysis
* **Streamlit** – Interactive web application
* **CSV** – Student data storage

## Beyond Syllabus Topic

### Streamlit – Interactive Web Application Development

**Streamlit** is used as the beyond-syllabus topic in this project.

It converts the Python data analysis program into an interactive web application. Users can enter student details, view records, remove students, and see statistics and charts through the Streamlit interface.

## Data Processing

The system accepts:

* Student ID
* Student Name
* Age
* Gender
* Attendance
* Study Hours
* Assignment Marks
* Internal Marks
* Practical Marks
* Final Exam Marks

The system calculates:

* Total Marks
* Average Marks
* Result

A student is considered **Pass** when the average marks are at least 50 and attendance is at least 75%.

## Project Structure

```text
Student-Management-System/
│
├── pds.py
├── student_dataset.csv
├── README.md
├── requirements.txt
└── screenshots/
```

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
streamlit
pandas
```

## How to Run

Run the following command:

```bash
python -m streamlit run pds.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

## Future Scope

The project can be extended by adding:

* Search Student
* Update Student
* Grade Calculation
* Subject-wise Analysis
* Database Connectivity
* Machine Learning-based Result Prediction

## Conclusion

The project demonstrates the practical use of **Python for Data Science** for student data management and analysis. It combines data handling, calculations, CSV storage, and visualization with **Streamlit** to create an interactive application.

## Author

**Name:** samarth Patel

**Subject:** Python for Data Science

**Project:** Student Performance Management System

**Project Type:** PBL 3 – Micro Project

**Beyond Syllabus:** Streamlit

