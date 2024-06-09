from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=255, unique=True)
    item = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_date = models.DateTimeField()

    def __str__(self):
        return self.order_id
