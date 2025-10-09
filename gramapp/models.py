from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()
    contact = models.BigIntegerField()
    photo = models.ImageField(upload_to='post_images/', blank=True, null=True)


    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()
    contact = models.BigIntegerField()
    photo = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.name