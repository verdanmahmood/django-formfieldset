**django-formfieldset** is a simple Django app that provides a mix-in class for admin-like fieldset rendering.


Features
========

- Fieldset functionality similar to ``ModelAdmin``
- Shorthand rendering functions with fieldsets both for whole forms and for individual fieldsets

  - render as ``P``
  - render as ``TABLE``
  - render as ``UL``

- Templates are class variables
- Overrides nothing in ``django.forms.Form``


Installation
============

#. Add ``"django-formfieldset"`` directory to your Python path.
#. Add ``"formfieldset"`` to your ``INSTALLED_APPS`` tuple found in
   your settings file. (optional - to be able to run tests)


Testing & Example
=================

There is an example project in the ``example/`` folder. To run
automated tests for django-formfieldset run the following command
in ``example/`` directory:

::

    python manage.py test formfieldset

To run the example project:

::

    python manage.py runserver

Then you can visit ``http://localhost:8000/`` to view the example.


Usage
=====

#. Create your form with ``FieldsetMixin``.
#. Add a ``fieldsets`` attribute to your form. See
   `admin docs <http://docs.djangoproject.com/en/dev/ref/contrib/admin/#fieldsets>`_
   for detailed explanation.
#. Render your form with fieldset enabled methods:

   -  You can use ``iter_fieldsets()`` for custom form rendering. It
      will yield ``Fieldset`` objects. ``Fieldset``\ s act as iterators for
      widgets in them.
   -  You can use ``as_fieldset_table()``, ``as_fieldset_ul()`` and
      ``as_fieldset_p()`` methods that act like built-in ``as_*`` method
      except fieldset support.


See Also
========

-  `django-form-utils <http://bitbucket.org/carljm/django-form-utils/>`_

