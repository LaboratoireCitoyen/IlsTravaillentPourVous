from django.views import generic

from deputes.models import Depute


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['depute_list'] = Depute.objects.all().order_by('nom')

        return context
