from django.db import models
from django.contrib.auth.models import User

# Models for Inventory Products and Orders.
CATEGORY = (
    ('Beer', 'Beer'),
    ('Wine', 'Wine'),
    ('Spirits', 'Spirits'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)


    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
