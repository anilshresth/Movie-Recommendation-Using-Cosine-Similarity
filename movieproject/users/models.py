from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'profile of user{self.user.username}'


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} likes {self.movie_id}"
