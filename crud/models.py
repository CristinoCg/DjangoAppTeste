from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    post = models.TextField()

    def __str__(self):
        return f'Post de {self.author}, data:{self.created}'


