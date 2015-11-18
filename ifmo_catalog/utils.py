from ifmo_catalog.models import *


def get_course_subject(course):
    subject = SubjectCourses.objects.get(course_id=course.id).subject
    return subject.name


def get_all_subjects():
    subjects = Subject.objects.all()
    names = map(lambda s: s.name, subjects)
    return sorted(names)
