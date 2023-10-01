====================
Django Vue Utilities
====================

Provides helpers and utilities for integrating with a Vue 
front-end, as described in `Cookiecutter Vue + Django`_

.. _Cookiecutter Vue + Django: https://github.com/ilikerobots/cookiecutter-vue-django

Quick start
-----------

1. Add "django_vue_utilities" to your INSTALLED_APPS setting:

.. code-block::python

    INSTALLED_APPS = [
        ...,
        "django_vue_utilities",
    ]


Settings
--------

Tailor the following settings to your Vue front-end.  The defaults are provided below.

.. code-block:: python

    VUE_FRONTEND_USE_TYPESCRIPT = False
    VUE_FRONTEND_USE_DEV_SERVER = settings.DEBUG
    VUE_FRONTEND_DEV_SERVER_URL = 'http://localhost:5173'
    VUE_FRONTEND_DEV_SERVER_PATH = 'src'
    VUE_FRONTEND_STATIC_PATH = 'vue'


Usage
-----

.. code-block:: django

   {% extends "base.html" %}

   {% load vue_utils %}

   {% block extra_js %}
     {# Import entrypoint JavaScript, choosing dev or static source depending on settings #}
     <script type="module" crossorigin src="{% vue_bundle_url 'my_vue_entrypoint' %}"></script>

     {# 'provide" strings which can 'injected' throughout the Vue app, including from within a pinia store #}
     {% url 'home' as homeUrl %}
     {% vue_provide 'homeUrl' homeUrl %}
   {% endblock %}




