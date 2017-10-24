from django.db import models
from baseapp.models import Recently

# Create your models here.


class Category(Recently):
    name = models.CharField(max_length=30, db_index=True, primary_key=True)
    slug = models.CharField(max_length=30, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Documentation(Recently):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    langue = models.CharField(max_length=5)
    author = models.CharField(max_length=30)
    copyright = models.ForeignKey(
        'Copyright',
        on_delete=models.CASCADE,
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )


    def __str__(self):
        return self.name

class Copyright(Recently):
    name = models.CharField(max_length=30, db_index=True)
    description = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.name
