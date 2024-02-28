from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=100, unique=True, verbose_name="Department")
    
    class Meta:
        verbose_name = "Profile User"

    def __str__(self):
        return self.user.username