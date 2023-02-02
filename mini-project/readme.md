## A) Students
- matric_number (PK)
- gender
- age
- course_id (FK)
- email

Desc: 

Student can view time table, Add course to semester.

## Lecturers
- staff_id (PK)
- gender
- age
- department_id
- email

## Users
- id (PK)
- username
- password
- role (Lecturer, student, admin)

## Admins
- id (PK)
- name
- email


## Subjects
- subject_id (PK)
- department_id (FK)
- credits
- compulsory: BITI, BITE

Desc:

Example: 

Evolutionary algorithm, DSA, Data Science.

FK on department to indicate this course is belong to which department. 

## Departments
- department_id (PK)
- name
- short_name (BITI, BITE...)

Desc:

Example: ICA, Interactive Media, Security

## subject_compulsory
- department_id
- subject_id

Desc:

BITI ... Data Science (Compulsory need to take)

BITI ... Artificial Intelligence (Compulsory need to take)

## Time_table
- id (PK)
- start_time
- end_time
- days (Sun - Sat)
- student_id
- course_id

One student has one and only one time table. The time table have date, start time, end_time, and course.

Use Case:
- Login to the system
  - If the user == lecturer:
    - Have the capabilities of CRUD to subject, department
    - When user add subject, they can set some course to be compulsory to a certain department

  - If the user == student:
    - Have the capabilities of crud to time-table (Add subject and course)




