from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class PersonalDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='PersonalDetails')
    FirstName = models.CharField(max_length=120,verbose_name='first name')
    LastName = models.CharField(max_length=120,verbose_name='last name')
    Father = models.CharField(max_length=120,verbose_name='father name')
    choices = [('male','MALE'),('female','FEMALE'),('transgender','TRANSGENDER')]
    Gender = models.CharField(choices=choices,blank = False,max_length=50,verbose_name='Gender')
    Dob = models.DateField()
    def get_personal_url(self):
        return "/setup/"
    def __str__(self):
        return '{name}'.format(name=self.user.username)
class QualificationDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='QualificationDetails')
    Matric = models.CharField(max_length=120,verbose_name='Matric')
    Inter = models.CharField(max_length=120,verbose_name='Inter')
    Gradute = models.CharField(max_length=120,verbose_name='Gradute')
    Other = models.CharField(max_length=120,verbose_name='Other',blank=True,null=True)
    College =models.CharField(max_length=120,verbose_name='College',blank=True,null=True)
    def get_qualification_url(self):
        return "/setup/qualification"
    def __str__(self):
        return '{name}'.format(name=self.user.username)
class LocationDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='LocationDetails')
    State = models.CharField(max_length=120,verbose_name='site')
    City = models.CharField(max_length=120,verbose_name='city')
    District = models.CharField(max_length=120,verbose_name='district')
    Village = models.CharField(blank=True,max_length=120,verbose_name='village')
    def get_location_url(self):
        return "/setup/location"
    def __str__(self):
        return '{name}'.format(name=self.user.username)
class ProfileDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='Profile',blank=True,null=True)
    MobileNo = models.PositiveIntegerField(verbose_name='Mobile No')
    image = models.ImageField(upload_to='profile_pic',default='profile_pic/Avatar.png',blank=True,null=True)
    def get_profile_url(self):
        return "/setup/setimage"

    def __str__(self):
        return '{name}'.format(name=self.user.username)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
