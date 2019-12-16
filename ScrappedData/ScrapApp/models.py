from django.db import models

class BrowseItems(models.Model):
    name=models.CharField(max_length=64,null=True)
    price=models.FloatField(default=0)
    description=models.TextField()
    image_link=models.CharField(max_length=200,null=False,unique=True)
    def __str__(self):
        return str(self.name)
# Create your models here.
