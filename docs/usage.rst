=====
Usage
=====

To use Django desktop app in a project, add it to your `INSTALLED_APPS`:

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
