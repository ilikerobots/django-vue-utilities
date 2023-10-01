.. _tests:

Tests
*****

`Continuous integration test results <https://travis-ci.org/ilikerobots/django-vue-utils>`_ are available online.

However, you can also test the source code.

.. code-block:: bash

   $ workon myvenv
   $ python manage.py test
   
   Creating test database for alias 'default'...
   ..........
   ----------------------------------------------------------------------
   Ran 10 tests in 0.713s

   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.
