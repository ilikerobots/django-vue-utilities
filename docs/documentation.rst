.. _documentation:

Documentation
*************

`Full documentation <https://django-vue-utils.readthedocs.io/>`_ is available online.

However, you can also build the documentation from source. Enter your `virtual environment <https://virtualenv.pypa.io/>`_.

.. code-block:: bash

   $ workon myvenv

Clone the code repository.

.. code-block:: bash

   $ git clone git@github.com:ilikerobots/django-vue-utils.git
   $ cd django-vue-utils/

Install `Sphinx <http://www.sphinx-doc.org/>`_, |sphinx-autobuild|_, and |sphinx_rtd_theme|_.

.. |sphinx-autobuild| replace:: ``sphinx-autobuild``
.. _sphinx-autobuild: https://pypi.python.org/pypi/sphinx-autobuild

.. |sphinx_rtd_theme| replace:: ``sphinx_rtd_theme``
.. _sphinx_rtd_theme: https://pypi.python.org/pypi/sphinx_rtd_theme

.. code-block:: bash

   $ pip install sphinx sphinx-autobuild sphinx_rtd_theme

Create an HTML build.

.. code-block:: bash

   $ (cd docs/ && make html)

Or use ``sphinx-autobuild`` to watch for live changes.

.. code-block:: bash

   $ sphinx-autobuild docs/ docs/_build_html

Open `127.0.0.1:8000 <http://127.0.0.1:8000>`_.
