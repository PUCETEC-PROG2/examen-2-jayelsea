from django.db import models

# Create your models here.

class Movie (models.Model):
    name = models.CharField(max_length=30, null=False)
    genere = models.CharField(max_length=30, null=False)
    year = models.IntegerField(null=False)
    director = models.CharField(max_length=30, null=False)
    sinopsis= models.CharField(max_length=80, null=False)
    
def __str__(self) -> str:
        return self.name