import pytest
from gap_analysis import gap_analysis  # Correct function import

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    student_info = {
        "name": "Alice",
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

    return student_info, enrolled_courses, peer_grades

def test_compute_gap_scores(sample_data):
    """Tests if gap scores and total gap are calculated correctly."""
    student_info, enrolled_courses, peer_grades = sample_data
    
    result = gap_analysis(student_info, enrolled_courses, peer_grades)
    
    expected_gap_scores = {
        "Embedded Systems": -0.5,
        "Artificial Intelligence": -0.75,
        "Computer Networks": 0.25,
        "Software Engineering": -0.25
    }
    expected_total_gap = -1.25
    
    assert result["GAP Scores"] == expected_gap_scores
    assert result["Total GAP Score"] == expected_total_gap

def test_no_gap_scenario():
    """Tests when the student already meets or exceeds all required grades."""
    student_info = {"name": "Bob"}
    enrolled_courses = {
        "Embedded Systems": 1.5,
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

    result = gap_analysis(student_info, enrolled_courses, peer_grades)
    
    # Extract the recommendation part
    assert result["Recommendations"] == "Exceeding Expectations - Great Work!"

def test_single_course_gap():
    """Tests with only one course having a gap."""
    student_info = {"name": "Charlie"}
    enrolled_courses = {"Embedded Systems": 2.5}
    peer_grades = {"Embedded Systems": 2.0}

    result = gap_analysis(student_info, enrolled_courses, peer_grades)

    assert result["GAP Scores"] == {"Embedded Systems": -0.5}
    assert result["Total GAP Score"] == -0.5

def test_empty_courses():
    """Tests if the program handles an empty course list properly."""
    student_info = {"name": "David"}
    enrolled_courses = {}
    peer_grades = {}

    result = gap_analysis(student_info, enrolled_courses, peer_grades)
    assert result == "No courses enrolled. No GAP analysis can be performed."

def test_no_enrolled_courses(sample_data):
    student_info, _, peer_grades = sample_data
    result = gap_analysis(student_info, {}, peer_grades)
    assert result == "No courses enrolled. No GAP analysis can be performed."

def test_no_grades_in_courses(sample_data):
    student_info, enrolled_courses, peer_grades = sample_data
    empty_grades = {course: None for course in enrolled_courses}
    result = gap_analysis(student_info, empty_grades, peer_grades)
    assert result == "No grades provided. Please update your records."

def test_no_peer_grades(sample_data):
    student_info, enrolled_courses, _ = sample_data
    result = gap_analysis(student_info, enrolled_courses, {})
    assert result == "No peer grade data available. Unable to analyze gaps."

def test_no_indicated_course_in_peer_grades(sample_data):
    student_info, enrolled_courses, _ = sample_data
    missing_peer_grades = {"Database Systems": 2.0}  # Course not in enrolled_courses
    result = gap_analysis(student_info, enrolled_courses, missing_peer_grades)
    assert result == "Peer grade data does not match enrolled courses. Please check the input data."

def test_incomplete_grade(sample_data):
    """Tests if the function correctly handles incomplete grades (INC)."""
    student_info, enrolled_courses, peer_grades = sample_data
    enrolled_courses["Embedded Systems"] = "INC"  # Set "Embedded Systems" to INC

    result = gap_analysis(student_info, enrolled_courses, peer_grades)

    assert result == "You need to complete 'Embedded Systems' before a GAP analysis can be done."

