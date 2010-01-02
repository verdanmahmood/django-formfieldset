import os
from django import template
from django.conf import settings
from django.template.loader import find_template_source
from django.template.loader import get_template_from_string
from django.utils.html import escape
from django.utils.safestring import mark_safe
try:
    from pygments import highlight
    from pygments.lexers import PythonLexer, HtmlDjangoLexer, HtmlLexer
    from pygments.formatters import HtmlFormatter
except ImportError:
    highlight = None
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
    rendered = template_obj.render(template.Context({'form': form(),
                                            'MEDIA_URL': settings.MEDIA_URL}))
    if highlight:
        formatter = HtmlFormatter()
        form_code = highlight(form_code, PythonLexer(), formatter)
        template_code = highlight(template_code, HtmlDjangoLexer(), formatter)
        rendered_code = highlight(rendered, HtmlLexer(), formatter)
    else:
        form_code = u'<pre>%s</pre>' % form_code
        tpl = u'<pre>&lt;form action="" method="POST"&gt;%s&lt;/form&gt;</pre>'
        template_code = tpl % template_code
        rendered_code = tpl % escape(rendered)
    return {
        'name': example_name,
        'form_code': mark_safe(form_code),
        'template': mark_safe(template_code),
        'rendered_code': mark_safe(rendered_code),
        'rendered': rendered,
    }
