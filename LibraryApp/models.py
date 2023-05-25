from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    copies = models.IntegerField()
    available = models.IntegerField()
    