from ifmo_catalog.models import *
from django.core.exceptions import ObjectDoesNotExist

def get_course_subject(course):
    try:
        subject = SubjectCourses.objects.get(course_id=course.id).subject
        return subject.name
    except ObjectDoesNotExist:
        return "None"


def get_all_subjects():
    subjects = Subject.objects.all()
    names = map(lambda s: s.name, subjects)
    return sorted(names)
