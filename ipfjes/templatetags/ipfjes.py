from django import template
from opal.templatetags.forms import extract_common_args

register = template.Library()

@register.inclusion_tag("templatetags/script_text.html", takes_context=True)
def script_text(context, text):
    return {"text":text, 'user': context.get('request').user}


@register.inclusion_tag("_helpers/select_object.html")
def select_object(**kwargs):
    ctx = extract_common_args(kwargs)
    ctx["lookuplist"] = kwargs.pop("lookuplist", ctx.get("lookuplist", None))
    ctx["default_null"] = kwargs.pop('default_null', True)
    return ctx
