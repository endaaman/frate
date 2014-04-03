# -*- encoding: utf-8 -*-

from django.utils.safestring import mark_safe


def custom_context(request):
    return {'css3': True,
            }

