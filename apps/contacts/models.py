from django.db import models
from django.utils import timezone


class Contacts(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    email =  models.CharField(max_length=255, null=True, default=None)
    subject = models.CharField(max_length=255, null=True, default=None)
    message = models.CharField(max_length=255, null=True, default=None) 
    date_created = models.DateTimeField(blank=True, null=True)


    def save(self, *args, **kwargs):

        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
     
        super(Contacts, self).save(*args, **kwargs)
        

    def __str__(self):
        return str(self.name)