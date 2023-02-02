from django.shortcuts import render
from .models import Director, Pelicula
# Create your views here.
def index(request):
    directores = Director.objects.all()
    data = []
    for director in directores:
        peliculas = Pelicula.objects.filter(director=director)
        data.append({"nombre": director.first_name + ' ' + director.last_name, "peliculas": peliculas})

    return render(
        request,
        'index.html',
        context={
            'data': data,
        }
    )

    