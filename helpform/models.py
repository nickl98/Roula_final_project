from django.db import models

# Create your models here.


class Question(models.Model):
    asked_by = models.CharField(max_length=254)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    answered_by = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
