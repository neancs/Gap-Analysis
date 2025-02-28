def gap_analysis(student_info, enrolled_courses, peer_grades):
    if not enrolled_courses:
        return "No courses enrolled. No GAP analysis can be performed."
    
    gap_scores = {}
    total_gap = 0.0
    missing_grades = False
    inc_courses = []  # To store courses with INC/(grade)

    for course, student_grade in enrolled_courses.items():
        peer_grade = peer_grades.get(course)

        if student_grade is None:
            missing_grades = True
            gap_scores[course] = "N/A"
            continue
        
        if isinstance(student_grade, str) and student_grade.startswith("INC"):
            try:
                # Extract the numeric grade after "INC/"
                actual_grade = float(student_grade.split("/")[1])
                student_grade = actual_grade
                inc_courses.append(course)
            except (IndexError, ValueError):
                return f"You need to complete '{course}' before a GAP analysis can be done."
        
        if peer_grade is None:
            continue
        
        gap_score = peer_grade - student_grade
        gap_scores[course] = round(gap_score, 2)
        total_gap += gap_score

    if not peer_grades:
        return "No peer grade data available. Unable to analyze gaps."
    
    if missing_grades:
        return "No grades provided. Please update your records."
    
    if not gap_scores:
        return "Peer grade data does not match enrolled courses. Please check the input data."
    
    recommendations = "Suggested courses to improve, strengths, and career fit" if total_gap < 0 else "Exceeding Expectations - Great Work!"
    
    return {
        "Total GAP Score": total_gap,
        "GAP Scores": gap_scores,
        "Recommendations": recommendations,
        "Incomplete Courses Considered": inc_courses if inc_courses else "None"
    }
