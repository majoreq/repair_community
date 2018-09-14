from django.db import models
from django.contrib.auth.models import User

STATUSES = (
    ('00', 'not assigned'),
    ('01', 'assigned'),
    ('02', 'waiting for device'),
    ('03', 'recived'),
    ('04', 'under repair'),
    ('05', 'under testing'),
    ('06', 'repair complete'),
    ('07', 'shipped back to client'),
    ('08', 'case closed'),
)


class Ticket(models.Model):
    device = models.CharField(max_length=128, verbose_name="device")
    description = models.TextField(verbose_name="description")
    assigned_to = models.ForeignKey(User, related_name="assigned_to", verbose_name="assigned to", on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="ticket_author", verbose_name="author", on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=2, choices=STATUSES, default='00')
    grade = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='grade', null=True)


class Offer(models.Model):
    author = models.ForeignKey(User, related_name="offer_author", verbose_name="author", on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name="price")
    ticket = models.ForeignKey(Ticket, verbose_name="ticket", on_delete=models.SET_NULL, null=True)
    message = models.TextField(verbose_name="message")


class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    from_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_who')
    to_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_who')
    content = models.CharField(max_length=256)
    readed = models.BooleanField(default=False)