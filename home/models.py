from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    tel = models.CharField(max_length=12)

    def __str__(self):
        return str(self.user)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'home', default='static/images/no-img.jpg')
    schedule = models.CharField(max_length=255, default="")
    contact = models.CharField(max_length=12 )
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    
