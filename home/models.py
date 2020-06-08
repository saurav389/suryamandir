from django.db import models
from django.conf import settings
# Create your models here.
class contactus(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=254)
    Number = models.IntegerField()
    Query = models.TextField(max_length=500)


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

class facebook(models.Model):
    userid = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return "{user}".format(user=self.userid)