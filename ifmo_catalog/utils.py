from ifmo_catalog.models import *


def get_mapped_index_courses(courses):
    mapped_courses = {
        "current": [],
        "upcoming": [],
        "ended": []
    }
    for course in courses:
        if course.has_started() and not course.has_ended():
            mapped_courses["current"].append(course)
        elif not course.has_started():
            mapped_courses["upcoming"].append(course)
        else:
            mapped_courses["ended"].append(course)

    if mapped_courses["current"] or mapped_courses["upcoming"]:
        mapped_courses["ended"] = []
    return mapped_courses


def get_course_categories_ids(course):
    categories = CategoryCourses.objects.filter(course_id=course.id)
    names = " ".join([c.category.id for c in categories])
    return names


def get_all_categories():
    categories = Category.objects.filter(parent=None)
    categories = [c for c in categories if c.category_set]
    return categories
