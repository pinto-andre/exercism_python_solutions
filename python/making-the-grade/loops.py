"""Functions for organizing and calculating student exam scores."""

from typing import List

def round_scores(student_scores: list[float | int]) -> list[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    :raises: TypeError - Student scores must be a list data type.
    """
    if not isinstance(student_scores, list):
        raise TypeError("Student scores must be a list data type.")
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    :raises: TypeError - Student scores must be a list data type.
    """
    if not isinstance(student_scores, list):
        raise TypeError("Student scores must be a list data type.")
    failing_grades = [grade for grade in student_scores if grade <= 40]
    return len(failing_grades)


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the
    provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    :raises: TypeError - Student scores must be a list data type.
    """
    if not isinstance(student_scores, list):
        raise TypeError("Student scores must be a list data type.")

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    :raises: TypeError - Highest value must be an integer.
    """
    if not isinstance(highest, int):
        raise TypeError("Highest value must be an integer.")

    interval = (highest - 40) // 4
    grade_thresholds = []
    bottom_grade = 41

    while bottom_grade < highest:
        grade_thresholds.append(bottom_grade)
        bottom_grade += interval
    return grade_thresholds



def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    :raises: TypeError - Student scores and student names must be a list data type.
    """
    if not isinstance(student_scores, List) or not isinstance(student_names, List):
        raise TypeError("Student scores and student names must be a list data type.")

    joint_lists = [
        f"{index+1}. {score_name}: {score}" 
        for index, (score_name, score) in enumerate(zip(student_names, student_scores))
    ]
    return joint_lists


def perfect_score(student_info: list[list[str, int]]) -> list[str, int]:
    """Create a list that contains the name and grade of the first student to make a 
    perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    if not isinstance(student_info, List):
        raise TypeError("Student info must be a list data type")
    perfect_grade = []
    for pair in student_info:
        if pair[1] == 100:
            perfect_grade.extend(pair)
            break
    return perfect_grade
