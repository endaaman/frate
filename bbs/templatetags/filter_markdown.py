# coding: utf-8

from django.template.defaultfilters import register
from django.template.defaultfilters import stringfilter

from django.conf import settings
import markdown2


HIGHLIGHT_CLASS_NAME = 'hilite'


@register.filter()
@stringfilter
def md2html(value):
    return markdown2.markdown(
        value,
        extras={'code-friendly': 1, 'fenced-code-blocks': {'css_class': HIGHLIGHT_CLASS_NAME}})