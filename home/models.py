from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank = True)
    messege = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Information(models.Model):
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.address1

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()


    def __str__(self):
        return self.name

class Portfoliocategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Portfoliocategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.TextField()
    body = models.TextField()
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    auther = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    views = models.IntegerField(default = 0)
    date = models.DateTimeField(null = True)

    def __str__(self):
        return self.title