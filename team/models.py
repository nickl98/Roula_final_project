from django.db import models

# Team Model


class Team(models.Model):
    name = models.CharField(max_length=254)
    college = models.CharField(max_length=254)
    years_experience = models.CharField(max_length=2)
    quote = models.CharField(max_length=254, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
