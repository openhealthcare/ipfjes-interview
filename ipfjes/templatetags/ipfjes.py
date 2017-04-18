from django import template

register = template.Library()

@register.inclusion_tag("templatetags/script_text.html")
def script_text(text):
    return {"text":text}
