=============================
Django desktop app
=============================

.. image:: https://badge.fury.io/py/django-desktopapp.svg
    :target: https://badge.fury.io/py/django-desktopapp

.. image:: https://travis-ci.org/phonkee/django-desktopapp.svg?branch=master
    :target: https://travis-ci.org/phonkee/django-desktopapp

.. image:: https://codecov.io/gh/phonkee/django-desktopapp/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/phonkee/django-desktopapp

Your project description goes here

Documentation
-------------

The full documentation is at https://django-desktopapp.readthedocs.io.

Quickstart
----------

Install Django desktop app::

    pip install django-desktopapp

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_dapp.apps.DjangoDappConfig',
        ...
    )

Add Django desktop app's URL patterns:

.. code-block:: python

    from django_dapp import urls as django_dapp_urls


    urlpatterns = [
        ...
        url(r'^', include(django_dapp_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
