from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')  # Redirects to the home page


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # Corrected to OneToOneField
    bio = models.TextField(max_length=250)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def __str__(self): 
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=250)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    categories = models.CharField(max_length=200, default='Others')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('article-details', args=[str(self.id)])

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="blog_comments", on_delete=models.CASCADE)
    body = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.author.username} commented on {self.post.title}"
    
class city(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Follower(models.Model):
    user = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.follower} follows {self.user}"