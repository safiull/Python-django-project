from django.db import models
from django.contrib.auth.models import User

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.FileField()
    details = models.TextField()

    def __str__(self):
        return self.name.username
        
class category(models.Model):
    name = models.CharField(max_length = 30)


    def __str__(self):
        return self.name

class article(models.Model):
    article_author = models.ForeignKey(author,on_delete= models.CASCADE)
    title = models.CharField(max_length = 40)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.FileField()
    body = models.TextField()
    category = models.ForeignKey(category,on_delete= models.CASCADE)

    def __str__(self):
        return self.title











