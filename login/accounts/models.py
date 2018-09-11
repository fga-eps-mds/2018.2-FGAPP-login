from django.db import models

# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField()

    class Meta:
        ordering = ('created',)
