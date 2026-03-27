from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # جديد

    def __str__(self):
        return self.title