.. _usage:

Usage
*****

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

