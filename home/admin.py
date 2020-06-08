from django.contrib import admin
from .models import contactus, SearchQuery, facebook
# Register your models here.
mymodel = [SearchQuery,contactus,facebook]
admin.site.register(mymodel)