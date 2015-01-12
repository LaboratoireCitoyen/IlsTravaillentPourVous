from django.core.urlresolvers import reverse
from django.db import models

import autoslug


class Depute(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    slug = autoslug.AutoSlugField(unique=True,
        populate_from=lambda instance: unicode(instance))

    def __unicode__(self):
        return '%s %s' % (self.prenom, self.nom)

    def get_absolute_url(self):
        return reverse('depute_depute_detail', args=(self.slug,))
