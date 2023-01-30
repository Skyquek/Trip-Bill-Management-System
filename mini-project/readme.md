## A) Students
- matric_number (PK)
- gender
- age
- course_id (FK)

Desc: 

Student can view time table, Add course to semester.

## B) Subjects
- subject_id (PK)
- department_id (FK)
- credits
- compulsory: BITI, BITE

Desc:

Example: 

Evolutionary algorithm, DSA, Data Science.

FK on department to indicate this course is belong to which department. 

## C) Departments
- department_id (PK)
- name
- short_name (BITI, BITE...)

Desc:

Example: ICA, Interactive Media, Security

## D) subject_compulsory
- department_id
- subject_id

Desc:

BITI ... Data Science (Compulsory need to take)

BITI ... Artificial Intelligence (Compulsory need to take)

## E) Time_table
- id (PK)
- 

