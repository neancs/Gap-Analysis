import pytest
from gap_analysis import GapAnalysis

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
    analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
    
    gap_scores, total_gap = analyzer.compute_gap_scores()
    
    expected_gap_scores = {
        "Embedded Systems": -0.5,
        "Artificial Intelligence": -0.75,
        "Computer Networks": 0.25,
        "Software Engineering": -0.25
    }
    expected_total_gap = -1.25
    
    assert gap_scores == expected_gap_scores
    assert total_gap == expected_total_gap

def test_generate_recommendations(sample_data):
    """Tests if recommendations return the expected structure."""
    student_info, enrolled_courses, peer_grades = sample_data
    analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
    
    recommendations, gap_scores = analyzer.generate_recommendations()
    
    assert "Courses to Improve" in recommendations
    assert "Career Fit Suggestions" in recommendations
    assert isinstance(recommendations["Courses to Improve"], list)
    assert isinstance(recommendations["Career Fit Suggestions"], str)

# ➤ Additional Simple Tests

def test_no_gap_scenario():
    """Tests when the student already meets or exceeds all required grades."""
    student_info = {"name": "Bob"}
    enrolled_courses = {"Math": 2.0, "Science": 1.5}
    peer_grades = {"Math": 2.0, "Science": 1.5}

    analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
    gap_scores, total_gap = analyzer.compute_gap_scores()

    assert gap_scores == {"Math": 0.0, "Science": 0.0}
    assert total_gap == 0.0

    recommendations, _ = analyzer.generate_recommendations()
    assert recommendations == "Exceeding Expectations – Great Work!"

def test_single_course_gap():
    """Tests with only one course having a gap."""
    student_info = {"name": "Charlie"}
    enrolled_courses = {"History": 2.5}
    peer_grades = {"History": 2.0}

    analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
    gap_scores, total_gap = analyzer.compute_gap_scores()

    assert gap_scores == {"History": -0.5}
    assert total_gap == -0.5

def test_empty_courses():
    """Tests if the program handles an empty course list properly."""
    student_info = {"name": "David"}
    enrolled_courses = {}
    peer_grades = {}

    analyzer = GapAnalysis(student_info, enrolled_courses, peer_grades)
    gap_scores, total_gap = analyzer.compute_gap_scores()

    assert gap_scores == {}
    assert total_gap == 0.0

    recommendations, _ = analyzer.generate_recommendations()
    assert recommendations == "Exceeding Expectations – Great Work!"
