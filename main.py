from gap_analysis import GapAnalysis

# Example Data (Based on Alice's GAP Calculation)
student_info = {
    "name": "Alice Anicas",
    "SR-Code": "21-0001",
    "program": "BS Computer Engineering",
    "year_level": "4th Year",
    "semester": "1st Semester"
}

enrolled_courses = {
    "Embedded Systems": 2.0,
    "Artificial Intelligence": 2.5,
    "Computer Networks": 1.75,
    "Software Engineering": 2.0
}

peer_grades = {
    "Embedded Systems": 1.5,
    "Artificial Intelligence": 1.75,
    "Computer Networks": 2.0,
    "Software Engineering": 1.75
}

# Running the Analysis
analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
gap_scores, total_gap = analyzer.compute_gap_scores()
recommendations, detailed_gaps = analyzer.generate_recommendations()

# Display Results
print("Student Information:", student_info)
print("GAP Scores:", gap_scores)
print("Total GAP Score:", total_gap)
print("Recommendations:", recommendations)
