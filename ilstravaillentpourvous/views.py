from django.views import generic
from django.db.models import Q

from deputes.models import Depute


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['depute_list'] = Depute.objects.all().order_by('nom')

        return context


class AutocompleteView(generic.TemplateView):
    template_name = 'autocomplete.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AutocompleteView, self).get_context_data(*args, **kwargs)

        q = self.request.GET.get('q', '')

        context['deputes'] = Depute.objects.filter(
            Q(nom__icontains=q)|Q(prenom__icontains=q))[:7]

        return context
