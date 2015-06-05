from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fileStorage = FileSystemStorage(location='static/pictures')


# Create your models here.

class Picture(models.Model):
    picture = models.ImageField(storage=fileStorage)
    user = models.ForeignKey(User, related_name='picture')
