from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()

    def __str__(self):
        return f'Name: {self.name}\nSlug: {self.slug}'


