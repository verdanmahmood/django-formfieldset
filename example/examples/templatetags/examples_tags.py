import os
from django import template
from django.template.loader import find_template_source
from django.template.loader import get_template_from_string
from examples import forms


register = template.Library()


def get_form(example_name):
    form_path = os.path.join(os.path.dirname(forms.__file__),
                             '%s.py' % example_name)
    form_code = open(form_path, 'rb').read()
    form_module = __import__('examples.forms.%s' % example_name,
                             globals(),
                             locals(),
                             ['ExampleForm'])
    return getattr(form_module, 'ExampleForm'), form_code


def get_template(example_name):
    template_name = 'examples/examples/%s.html' % example_name
    template_code, origin = find_template_source(template_name)
    template_obj = get_template_from_string(template_code, origin, example_name)
    return template_obj, template_code


@register.inclusion_tag('examples/_example.html')
def example(example_name):
    form, form_code = get_form(example_name)
    template_obj, template_code = get_template(example_name)
    return {
        'name': example_name,
        'form_code': form_code,
        'template': template_code,
        'rendered': template_obj.render(template.Context({'form': form()}))
    }
