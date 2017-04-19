from django import template

register = template.Library()

@register.inclusion_tag("templatetags/script_text.html", takes_context=True)
def script_text(context, text):
    return {"text":text, 'user': context.get('request').user}
