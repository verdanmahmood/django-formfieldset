from django.test import TestCase
from django import forms as django_forms
import forms


class FieldsetRenderTestCase(TestCase):
    def setUp(self):
        class TestForm(django_forms.Form, forms.FieldsetMixin):
            test_field1 = django_forms.CharField()
            test_field2 = django_forms.CharField()
            test_field3 = django_forms.CharField()
            test_field4 = django_forms.CharField(
                                      widget=django_forms.widgets.HiddenInput)

            fieldsets = (
                (u'Fieldset1', {
                    'description': u'Test Description',
                    'fields': ('test_field1',),
                }),
                (u'Fieldset2', {
                    'fields': ('test_field2', 'test_field3', 'test_field4'),
                }),
            )

            def clean_test_field2(self):
                if self.cleaned_data['test_field2'] != u'':
                    raise django_forms.ValidationError(
                                    [u'Test Error - Field Level - 1',
                                    u'Test Error - Field Level - 2'])

            def clean(self):
                raise django_forms.ValidationError(u'Test Error - Top Level')
        self.test_form = TestForm

    def test_fieldset_render(self):
        """Test if the form is being rendered at all and all the elements are
           in the result.
        """
        form = self.test_form(data={'test_field2': u'Test Value'})
        self.assertEqual(form.is_valid(), False)
        for method in ('as_fieldset_table', 'as_fieldset_ul', 'as_fieldset_p'):
            rendered = getattr(form, method)()
            # Are all errors rendered somehow?
            self.assertTrue(u'Test Error - Top Level' in rendered)
            self.assertTrue(u'Test Error - Field Level - 1' in rendered)
            self.assertTrue(u'Test Error - Field Level - 2' in rendered)
            # Are all fields present?
            for field in form.fields.keys():
                bf= django_forms.forms.BoundField(form,
                                                  form.fields[field],
                                                  field)
                self.assertTrue(unicode(bf) in rendered)
            # Check for fieldset titles & decriptions
            self.assertTrue(u'Fieldset1' in rendered)
            self.assertTrue(u'Fieldset2' in rendered)
            self.assertTrue(u'Test Description' in rendered)
