from django import template
register = template.Library()

@register.filter
def first_matching_group(groups, course):
    for group in groups:
        if group.topic == course:
            return group
    return None