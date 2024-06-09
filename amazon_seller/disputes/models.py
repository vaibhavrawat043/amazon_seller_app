from django.db import models
from returns.models import Return

class Dispute(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved')
    ]

    return_order = models.ForeignKey(Return, on_delete=models.CASCADE)
    dispute_reason = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    resolution = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dispute for Return {self.return_order.id}"
