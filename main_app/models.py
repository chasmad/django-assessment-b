from django.db import models

class Item(models.Model):
    description = models.TextField(max_length=100)
