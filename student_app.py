import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Student Management System', layout='wide')
FILE = 'student_management_system.csv'
COLUMNS = ['Student_ID', 'Student_Name', 'Gender', 'Age', 'Course', 'Semester',
           'Email', 'Attendance_Percentage', 'Marks_Percentage', 'Status']


def load_data():
    if os.path.exists(FILE):
        data = pd.read_csv(FILE, dtype={'Student_ID': str})
        for col in COLUMNS:
            if col not in data.columns:
                data[col] = pd.NA
        return data[COLUMNS]
    return pd.DataFrame(columns=COLUMNS)


def save_data(data):
    data.to_csv(FILE, index=False)


df = load_data()
st.title('Student Management System')
st.header('Student Records')
st.dataframe(df, use_container_width=True, hide_index=True)
st.divider()
operation = st.radio('Select Operation',
                     ['Add', 'Search', 'Update', 'Delete', 'Analysis', 'Graph'],
                     horizontal=True)

if operation == 'Add':
    st.subheader('Add Student')
    with st.form('add_form'):
        student_id = st.text_input('Student ID')
        name = st.text_input('Student Name')
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
        age = st.number_input('Age', min_value=1, max_value=100, value=19)
        course = st.selectbox('Course', ['Computer Engineering', 'Information Technology', 'Other'])
        semester = st.number_input('Semester', min_value=1, max_value=8, value=5)
        email = st.text_input('Email')
        attendance = st.number_input('Attendance (%)', min_value=0.0, max_value=100.0, value=75.0)
        marks = st.number_input('Marks (%)', min_value=0.0, max_value=100.0, value=70.0)
        status = st.selectbox('Status', ['Active', 'Inactive'])
        submitted = st.form_submit_button('Add Student')
    if submitted:
        student_id, name, email = student_id.strip(), name.strip(), email.strip()
        if not student_id or not name or not email:
            st.error('Student ID, name and email are required.')
        elif student_id in df['Student_ID'].astype(str).values:
            st.error('Student ID already exists.')
        else:
            new_student = pd.DataFrame([{
                'Student_ID': student_id, 'Student_Name': name, 'Gender': gender,
                'Age': age, 'Course': course, 'Semester': semester, 'Email': email,
                'Attendance_Percentage': attendance, 'Marks_Percentage': marks,
                'Status': status
            }])
            save_data(pd.concat([df, new_student], ignore_index=True))
            st.success('Student added successfully.')
            st.rerun()

elif operation == 'Search':
    st.subheader('Search Student')
    student_id = st.text_input('Enter Student ID').strip()
    if st.button('Search'):
        result = df[df['Student_ID'].astype(str) == student_id]
        if result.empty:
            st.warning('Student not found.')
        else:
            st.dataframe(result, use_container_width=True, hide_index=True)

elif operation == 'Update':
    st.subheader('Update Student')
    student_id = st.text_input('Enter Student ID').strip()
    if st.button('Find Student'):
        result = df[df['Student_ID'].astype(str) == student_id]
        if result.empty:
            st.warning('Student not found.')
            st.session_state.pop('update_id', None)
        else:
            st.session_state['update_id'] = student_id
    update_id = st.session_state.get('update_id')
    matches = df.index[df['Student_ID'].astype(str) == update_id] if update_id else []
    if len(matches):
        idx = matches[0]
        student = df.loc[idx]
        with st.form('update_form'):
            name = st.text_input('Student Name', value=str(student['Student_Name']))
            gender_options = ['Male', 'Female', 'Other']
            gender = st.selectbox('Gender', gender_options,
                                  index=gender_options.index(student['Gender']) if student['Gender'] in gender_options else 2)
            age = st.number_input('Age', 1, 100, int(student['Age']))
            course = st.text_input('Course', value=str(student['Course']))
            semester = st.number_input('Semester', 1, 8, int(student['Semester']))
            email = st.text_input('Email', value=str(student['Email']))
            attendance = st.number_input('Attendance (%)', 0.0, 100.0,
                                         float(student['Attendance_Percentage']))
            marks = st.number_input('Marks (%)', 0.0, 100.0,
                                    float(student['Marks_Percentage']))
            status_options = ['Active', 'Inactive']
            status = st.selectbox('Status', status_options,
                                  index=status_options.index(student['Status']) if student['Status'] in status_options else 0)
            submitted = st.form_submit_button('Update Student')
        if submitted:
            if not name.strip() or not email.strip() or not course.strip():
                st.error('Name, course and email are required.')
            else:
                df.loc[idx, COLUMNS[1:]] = [name.strip(), gender, age, course.strip(), semester,
                                            email.strip(), attendance, marks, status]
                save_data(df)
                del st.session_state['update_id']
                st.success('Student updated successfully.')
                st.rerun()

elif operation == 'Delete':
    st.subheader('Delete Student')
    student_id = st.text_input('Enter Student ID').strip()
    if st.button('Delete Student'):
        result = df[df['Student_ID'].astype(str) == student_id]
        if result.empty:
            st.warning('Student not found.')
        else:
            save_data(df[df['Student_ID'].astype(str) != student_id])
            st.success('Student deleted successfully.')
            st.rerun()

elif operation == 'Analysis':
    st.subheader('Student Data Analysis')
    if df.empty:
        st.info('Add students to view analysis.')
    else:
        marks = pd.to_numeric(df['Marks_Percentage'], errors='coerce')
        attendance = pd.to_numeric(df['Attendance_Percentage'], errors='coerce')
        c1, c2, c3 = st.columns(3)
        c1.metric('Total Students', len(df))
        c2.metric('Average Marks', f'{marks.mean():.2f}%')
        c3.metric('Average Attendance', f'{attendance.mean():.2f}%')
        c4, c5, c6 = st.columns(3)
        c4.metric('Highest Marks', f'{marks.max():.2f}%')
        c5.metric('Lowest Marks', f'{marks.min():.2f}%')
        c6.metric('Active Students', int((df['Status'] == 'Active').sum()))
        st.write('Students by Course')
        st.dataframe(df['Course'].value_counts().rename('Students'), use_container_width=True)
        st.write('Students by Status')
        st.dataframe(df['Status'].value_counts().rename('Students'), use_container_width=True)

elif operation == 'Graph':
    st.subheader('Student Performance Graphs')
    if df.empty:
        st.info('Add students to view graphs.')
    else:
        marks = pd.to_numeric(df['Marks_Percentage'], errors='coerce')
        attendance = pd.to_numeric(df['Attendance_Percentage'], errors='coerce')
        fig1, ax1 = plt.subplots()
        ax1.bar(df['Student_Name'], marks)
        ax1.set(title='Student Marks', xlabel='Student', ylabel='Marks (%)', ylim=(0, 100))
        ax1.tick_params(axis='x', labelrotation=45)
        fig1.tight_layout()
        st.pyplot(fig1)
        plt.close(fig1)

        fig2, ax2 = plt.subplots()
        ax2.hist(marks.dropna(), bins=5)
        ax2.set(title='Marks Distribution', xlabel='Marks (%)', ylabel='Number of Students')
        st.pyplot(fig2)
        plt.close(fig2)

        fig3, ax3 = plt.subplots()
        df['Course'].value_counts().plot(kind='bar', ax=ax3)
        ax3.set(title='Students by Course', xlabel='Course', ylabel='Number of Students')
        ax3.tick_params(axis='x', labelrotation=25)
        fig3.tight_layout()
        st.pyplot(fig3)
        plt.close(fig3)

        fig4, ax4 = plt.subplots()
        ax4.scatter(attendance, marks)
        ax4.set(title='Attendance vs Marks', xlabel='Attendance (%)', ylabel='Marks (%)',
                xlim=(0, 100), ylim=(0, 100))
        st.pyplot(fig4)
        plt.close(fig4)

st.caption('Python for Data Science — Student Management System')
