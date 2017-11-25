from django.db import models

# Create your models here.
from django.db import models
from index.models import User
# Create your models here.


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField()
    start_date = models.DateTimeField()
    last_send = models.DateTimeField(null=True)
    next_send = models.DateTimeField()
    interval = models.IntegerField(null=True, default=1)
    interval_type = models.CharField(max_length=50, null=True, default='week(s)')
    snooze = models.NullBooleanField(null=True)
    snooze_interval = models.IntegerField(null=True)
    snooze_interval_type = models.CharField(max_length=50, null=True)
    snooze_last_send = models.DateTimeField(null=True)
    snooze_next_send = models.DateTimeField(null=True)
    in_deleted = models.BooleanField(default=False)
    notification_method = models.CharField(default='text', max_length=10)
    interval_type.choices = (
        ('day', 'day(s)'),
        ('week', 'week(s)'),
        ('month', 'month(s)'),
        ('year', 'year(s)')
    )
    notification_method.choices = (
        ('text', 'text'),
        ('email', 'email'),
        ('both', 'both')
    )


class MessageLogPerson(models.Model):
    user_id = models.IntegerField(null=True)
    person_id = models.IntegerField(null=True)
    sent = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=50)