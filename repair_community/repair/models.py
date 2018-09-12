from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    device = models.CharField(max_length=128, verbose_name="device")
    description = models.TextField(verbose_name="description")
    assigned_to = models.ForeignKey(User, related_name="assigned_to", verbose_name="assigned to", on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="author", verbose_name="author", on_delete=models.SET_NULL, null=True)

