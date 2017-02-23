from django.db import models


# Create your models here.

# Model of an Item
class Item(models.Model):
    item_name = models.CharField(max_length=100, blank=False, null=False)


class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)
