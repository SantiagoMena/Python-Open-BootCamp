from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Pelicula(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text='Describe la pelicula')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('pelicula-detail', args=[str(self.id)])

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    peliculas = models.ManyToOneRel('director', Pelicula, 'director')

    def __str__(self) -> str:
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])
