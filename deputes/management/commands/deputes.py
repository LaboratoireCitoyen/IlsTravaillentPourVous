import ijson.backends.yajl2 as ijson

from django.core.management.base import BaseCommand

from ...models import Depute


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.deputes = []
        for depute in Depute.objects.values_list('nom', 'prenom', 'pk'):
            self.deputes.append(depute[0]+depute[1])

        for source in args:
            with open(args[0], 'r') as f:
                for item in ijson.items(f, 'item'):
                    if item['nom'] + item['prenom'] in self.deputes:
                        continue

                    depute, created = Depute.objects.get_or_create(
                        nom=item['nom'], prenom=item['prenom'])

                    self.deputes.append(item['nom']+item['prenom'])
