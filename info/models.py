from django.db import models

# Create your models here.
class mainNews(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

class cardNews(models.Model):
    datetime = models.DateField()
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to="image/")
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title