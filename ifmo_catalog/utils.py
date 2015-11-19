from ifmo_catalog.models import *
from lms.djangoapps.courseware.courses import get_courses


def get_course_subjects(course):
    subjects = SubjectCourses.objects.filter(course_id=course.id)
    names = " ".join([s.subject.name for s in subjects])
    return names


def get_all_subjects():
    subjects = Subject.objects.filter(parent=None)
    subjects = [s for s in subjects if s.subject_set]
    return subjects


def get_courses_availability(user):
    courses = get_courses(user)
    return reduce(lambda (up, curr), course: (
        up or not course.has_started(),  # upcoming courses
        curr or (course.has_started() and not course.has_ended())  # current courses
    ), courses, (False, False))