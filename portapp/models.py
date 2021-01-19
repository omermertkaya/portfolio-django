from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.urls import reverse



# Create your models here.


class WebLogoName(models.Model):
    web_name = models.CharField(max_length=225,help_text="This is your site title")
    web_logo = models.ImageField(null= True, blank=True)


class HomeSection(models.Model):

    cv_name_surname = models.CharField(max_length=225)
    cv_job = models.CharField(max_length=225, default ="blog")
    cv_photo= models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse('home')
    def __str__(self):
        return self.cv_name_surname + ' | ' + str(self.author)
        

    
class MyServicesSection(models.Model):
    title_1 = models.CharField(max_length=255)
    content_1 = RichTextField(blank=True, null=True)
    title_2 = models.CharField(max_length=255)
    content_2 = RichTextField(blank=True, null=True)
    title_3 = models.CharField(max_length=255)
    content_3 = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str(self):
        return self.author


class AboutMeSection(models.Model):
    who_title = models.CharField(max_length=255,help_text="Who I am; under the title")
    who_content = RichTextField(blank=True, null=True)
    who_photo = models.ImageField(null=True, blank=True)





class StorySection(models.Model):
    story_title = models.CharField(max_length=255, help_text="This is My Story; under the title")
    story_content = RichTextField(blank=True, null=True)
    story_photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.story_title + '   | Story Bolumu'



class WorkSection(models.Model):
    work_name = models.CharField(max_length=255)
    work_sub_title_black =  models.CharField(max_length=255, blank=True)
    work_sub_title = models.CharField(max_length=255, blank=True)
    work_article_photo = models.ImageField(null=True, blank=True)
    work_index_photo = models.ImageField(null=True, blank=True, help_text="Upload 400x400 images to get a good look.")
    work_content = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.work_name + '|' + str(self.work_index_photo)
    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))
    
class FooterSection(models.Model):
    footer_linked = models.CharField(max_length=300, blank=True)
    footer_github = models.CharField(max_length=300, blank=True)
    footer_instagram = models.CharField(max_length=300, blank=True)
    footer_facebook = models.CharField(max_length=300, blank=True)
    footer_email = models.CharField(max_length=300, blank=True)