from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "The book {} costs: {}".format(self.title, self.value)
