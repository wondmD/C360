from django import template

register = template.Library()

@register.filter
def first_matching_group(groups, cource):
    for group in groups:
        if group.topic == cource:
            return group
    return None
