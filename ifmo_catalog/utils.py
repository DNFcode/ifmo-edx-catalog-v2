from ifmo_catalog.models import *


def get_course_subjects(course):
    subjects = SubjectCourses.objects.filter(course_id=course.id)
    names = " ".join([s.subject.name for s in subjects])
    return names


def get_all_subjects():
    subjects = Subject.objects.filter(parent=None)
    subjects = [s for s in subjects if s.subject_set]
    return subjects
