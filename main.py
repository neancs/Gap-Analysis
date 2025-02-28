from gap_analysis import gap_analysis

student_info = {
    "name": "Alice",
    "SR-Code": "21-0001",
    "program": "BS Computer Engineering",
    "year_level": "4th Year",
    "semester": "1st Semester"
}

enrolled_courses = {
    "Embedded Systems": "INC",
    "Artificial Intelligence": 1.75,
    "Computer Networks": 2.0,
    "Software Engineering": 1.75
}

peer_grades = {
    "Embedded Systems": 1.5,
    "Artificial Intelligence": 1.75,
    "Computer Networks": 2.0,
    "Software Engineering": 1.75
}

# Perform GAP Analysis
result = gap_analysis(student_info, enrolled_courses, peer_grades)
print(result)