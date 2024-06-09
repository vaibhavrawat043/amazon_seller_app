from django.db import models
from orders.models import Order

class Return(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_tracking = models.CharField(max_length=255)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"Return for Order {self.order.order_id}"
