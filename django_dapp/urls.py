# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_dapp'
urlpatterns = [
    url(
        regex="^Application/~create/$",
        view=views.ApplicationCreateView.as_view(),
        name='Application_create',
    ),
    url(
        regex="^Application/(?P<pk>\d+)/~delete/$",
        view=views.ApplicationDeleteView.as_view(),
        name='Application_delete',
    ),
    url(
        regex="^Application/(?P<pk>\d+)/$",
        view=views.ApplicationDetailView.as_view(),
        name='Application_detail',
    ),
    url(
        regex="^Application/(?P<pk>\d+)/~update/$",
        view=views.ApplicationUpdateView.as_view(),
        name='Application_update',
    ),
    url(
        regex="^Application/$",
        view=views.ApplicationListView.as_view(),
        name='Application_list',
    ),
	url(
        regex="^Release/~create/$",
        view=views.ReleaseCreateView.as_view(),
        name='Release_create',
    ),
    url(
        regex="^Release/(?P<pk>\d+)/~delete/$",
        view=views.ReleaseDeleteView.as_view(),
        name='Release_delete',
    ),
    url(
        regex="^Release/(?P<pk>\d+)/$",
        view=views.ReleaseDetailView.as_view(),
        name='Release_detail',
    ),
    url(
        regex="^Release/(?P<pk>\d+)/~update/$",
        view=views.ReleaseUpdateView.as_view(),
        name='Release_update',
    ),
    url(
        regex="^Release/$",
        view=views.ReleaseListView.as_view(),
        name='Release_list',
    ),
	]
