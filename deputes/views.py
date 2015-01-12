from django.views import generic

from .models import Depute


class DeputeDetailView(generic.DetailView):
    model = Depute
