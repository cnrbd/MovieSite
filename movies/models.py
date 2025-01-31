from django.db import models

# Create your models here.
class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/',  blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

