from django.db import models


# Create your models here.

# Model of an Item
class Item(models.Model):
    item_name = models.CharField(max_lenght=100)
    objects = ItemManager()


class ItemManager(models.Manager):

    def create_item(self, item_name):
        item = self.create(item_name=item_name)
