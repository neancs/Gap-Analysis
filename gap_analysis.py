class GapAnalysis:
    def __init__(self, student_info, enrolled_courses, peer_grades):
        self.student_info = student_info  # Dictionary with student details
        self.enrolled_courses = enrolled_courses  # {course_name: current_grade}
        self.peer_grades = peer_grades  # {course_name: required_grade}

    def compute_gap_scores(self):
        gap_scores = {}
        total_gap_score = 0

        for course, current_grade in self.enrolled_courses.items():
            required_grade = self.peer_grades.get(course, current_grade)  # Get highest peer grade
            gap = required_grade - current_grade
            gap_scores[course] = gap
            total_gap_score += gap

        return gap_scores, total_gap_score

    def generate_recommendations(self):
        gap_scores, total_gap = self.compute_gap_scores()

        if total_gap >= 0:
            return "Exceeding Expectations – Great Work!", {}

        sorted_gaps = sorted(gap_scores.items(), key=lambda x: x[1])  # Sort by lowest gap first
        recommendations = {
            "Courses to Improve": [course for course, gap in sorted_gaps if gap < 0],
            "Career Fit Suggestions": "Focus on strengthening weak areas for career growth."
        }

        return recommendations, gap_scores




