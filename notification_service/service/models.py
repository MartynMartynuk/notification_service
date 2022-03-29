from django.db import models
import pytz


class MailingList(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    message_text = models.TextField()
    client_filter = models.CharField(max_length=255)
    end_time = models.DateTimeField(verbose_name='Окончание рассылки')


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.IntegerField()
    operator_code = models.IntegerField()
    tag = models.CharField(max_length=20)
    timezone = models.CharField(max_length=6, default='UTC')


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    sending_status = models.BooleanField()
    mailinglist_id = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
