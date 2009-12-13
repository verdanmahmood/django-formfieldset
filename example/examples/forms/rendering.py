from django import forms
from formfieldset.forms import FieldsetMixin


RATING_CHOICES = (
    ('NR', u'Unrated'),
    ('G', u'General Audiences [G]'),
    ('PG', u'Parental Guidance Suggested [PG]'),
    ('PG-13', u'Parents Strongly Cautioned [PG-13]'),
    ('R', u'Restricted [R]'),
    ('NC-17', u'No One 17 and Under Admitted [NC-17]'),
)


class ExampleForm(forms.Form, FieldsetMixin):
    """A form for our movie database"""
    fieldsets = (
        (None, {'fields': ('title', 'genre', 'mpaa_rating')}),
        (u'Plot', {'fields': ('plot_summary', 'keywords'),
                   'description': u'These fields will be '
                                  u'used in movie search.'}),
        (u'Other Details', {'fields': ('release_year',
                                       'imdb_score',
                                       'official_website')})
    )

    title = forms.CharField()
    genre = forms.ChoiceField(choices=(('ac', u'Action'),
                                       ('dr', u'Drama'),
                                       ('co', u'Comedy')))
    mpaa_rating = forms.ChoiceField(choices=RATING_CHOICES,
                                    label=u'MPAA rating')
    plot_summary = forms.CharField(widget=forms.widgets.Textarea)
    keywords = forms.CharField(help_text=u'Seperate multiple tags with commas.')
    release_year = forms.ChoiceField(choices=(('2008', u'2008'),
                                            ('2009', u'2009'),
                                            ('2010', u'2010')))
    imdb_score = forms.CharField(label=u'IMDB score')
    official_website = forms.URLField()
