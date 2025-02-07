from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/',  blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Review (models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.movie.name}"
