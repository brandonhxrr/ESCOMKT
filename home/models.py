from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    tel = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)
