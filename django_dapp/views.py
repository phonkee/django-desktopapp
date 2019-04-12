# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Application,
	Release,
)


class ApplicationCreateView(CreateView):

    model = Application


class ApplicationDeleteView(DeleteView):

    model = Application


class ApplicationDetailView(DetailView):

    model = Application


class ApplicationUpdateView(UpdateView):

    model = Application


class ApplicationListView(ListView):

    model = Application


class ReleaseCreateView(CreateView):

    model = Release


class ReleaseDeleteView(DeleteView):

    model = Release


class ReleaseDetailView(DetailView):

    model = Release


class ReleaseUpdateView(UpdateView):

    model = Release


class ReleaseListView(ListView):

    model = Release

