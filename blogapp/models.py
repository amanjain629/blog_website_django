from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Catagory(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        # return reverse("article-detail",args=(str(self.id)))
        return reverse("index")

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url=models.CharField(max_length=255,null=True, blank=True)
    fb_url=models.CharField(max_length=255,null=True, blank=True)
    twitter_url=models.CharField(max_length=255,null=True, blank=True)
    instagram_url=models.CharField(max_length=255,null=True, blank=True)
    pinterest_url=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    catagory=models.CharField(max_length=255,default='coding')
    body=RichTextField(blank=True,null=True)
    # body=models.TextField()
    date_post=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # return reverse("article-detail",args=(str(self.id)))
        return reverse("index")
    