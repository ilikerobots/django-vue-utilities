.. _index:
.. module:: django-vue-utils

Django Vue Utils
****************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-vue-utils.svg
.. _PyPI version: https://pypi.python.org/pypi/django-vue-utils

.. |Build status| image::
   https://travis-ci.org/ilikerobots/django-vue-utils.svg?branch=master
.. _Build status: https://travis-ci.org/ilikerobots/django-vue-utils

**Django Vue Utils** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/>`_ collection for use with a Vue integration as described in `Cookiecutter Vue + Django <https://github.com/ilikerobots/cookiecutter-vue-django>`_

* `Package distribution <https://pypi.python.org/pypi/django-vue-utils>`_
* `Code repository <https://github.com/ilikerobots/django-vue-utils>`_
* `Documentation <https://django-vue-utils.readthedocs.io/>`_
* `Tests <https://travis-ci.org/ilikerobots/django-vue-utils>`_

Install
=======

.. code-block:: bash

   $ pip install django-vue-utils

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'django_vue_utils',
   ]

Usage
=====

.. code-block:: django

   {% load vue_utils %}

   {% block extra_js %}
    {# Import entrypoint JavaScript, choosing dev or static source depending on settings #}
    <script type="module" crossorigin src="{% vue_bundle_url 'my_vue_entrypoint' %}"></script>

    {# 'provide" strings which can 'injected' throughout the Vue app, including from within a pinia store #}
    {% url 'home' as homeUrl %}
    {% vue_provide 'homeUrl' homeUrl %}
   {% endblock %}

Contents
========

.. toctree::
   :maxdepth: 2

   install
   usage
   documentation
   tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
