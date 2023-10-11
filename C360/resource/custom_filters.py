from django import template


register = template.Library()

@register.filter
def has_liked_course(course, user):
    return course.courselike_set.filter(user=user).exists()