from django.db import models

class ShopItems(models.Model):
    name = models.CharField(max_length=100)
    new_price = models.DecimalField(max_digits=5, decimal_places=1)
    old_price = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_offered = models.BooleanField(default=False)
    offer_percent = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

