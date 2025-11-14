Python_students = {"Alice","Bob","Raj"}
Data_science_students = {"Ravi","Rahul","Raj","Ajay"}
Python_students.add("Sujith")
Data_science_students.remove("Ajay")
both_courses = Python_students & Data_science_students
print("Students in both courses",both_courses)
only_python = Python_students - Data_science_students
print("Students only in Python",only_python)
all_students = Python_students | Data_science_students
print("All students in either course:",all_students)
course_counts = {"Python": len(Python_students), "Data Science": len(Data_science_students)}
for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")
expected_growth = {course: count * 2 for course, count in course_counts.items()}
print("Expected growth:", expected_growth)
    