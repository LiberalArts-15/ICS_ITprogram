from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30, 
        unique=True,
        null=True,
        error_messages={'unique': 'すでに存在しているユーザーネームです。'},
        )
    
    profile_pic = models.ImageField(
        default = "default_profile_pic.jpg", upload_to="profile_pics"
        )
    
    intro = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=30)
    keyword = models.CharField(max_length=50)

    CATEGORY_CHOICES = [
        ('all', '自由'),
        ('minutes', '会議録'),
        ('notice', 'お知らせ'),
    ]
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        default='all',
    )
    
    image1 = models.ImageField(upload_to="post_pics", blank=True)
    image2 = models.ImageField(upload_to="post_pics", blank=True)
    image3 = models.ImageField(upload_to="post_pics", blank=True)
    
    content = models.TextField()
    
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title