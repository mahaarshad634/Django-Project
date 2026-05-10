from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=22)
#     blog = models.CharField(max_length=1000)


# class person(models.Model):
#     name=models.CharField(max_length=22)
#     rool_no=models.IntegerField()

class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='myapp/static/images', blank=True, null=True)
      
class userr(models.Model):
    name= models.CharField(max_length=22)
    username= models.CharField(max_length=33)
    password= models.CharField(max_length=14)      

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"