from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class PostHome2(models.Model):

    cv_isim_soyisim = models.CharField(max_length=225)
    cv_Meslek = models.CharField(max_length=225, default ="blog")
    cv_fotograf_1 = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.cv_isim_soyisim+ ' | ' + str(self.author)

    
class PostHome3(models.Model):
    baslik_1 = models.CharField(max_length=255)
    aciklama_1 = models.TextField()
    baslik_2 = models.CharField(max_length=255)
    aciklama_2 = models.TextField()
    baslik_3 = models.CharField(max_length=255)
    aciklama_3 = models.TextField()
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str(self):
        return self.author


class PostHome4(models.Model):
    who_baslik = models.CharField(max_length=255)
    who_aciklama = models.TextField()
    who_fotograf = models.ImageField(null=True, blank=True)





class Story_Bolumu(models.Model):
    story_baslik = models.CharField(max_length=255)
    story_aciklama = models.TextField()
    story_fotograf = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.story_baslik + '   | Story Bolumu'



class Work_Bolumu(models.Model):
    work_isim = models.CharField(max_length=255)
    work_alt_baslik = models.CharField(max_length=255, blank=True)
    work_fotograf = models.ImageField(null=True, blank=True)
    work_fotograf_3 = models.ImageField(null=True, blank=True)
    work_aciklama = models.TextField()
    
    def __str__(self):
        return self.work_isim + '|' + str(self.work_fotograf)
    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))
    
