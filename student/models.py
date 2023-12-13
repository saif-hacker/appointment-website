from django.db import models

# Create your models here.

class ContactModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    desc = models.TextField()
    
    def __str__(self):
        return self.fname
    
    class Meta:
        ordering = ['fname']
        
class Sign_up(models.Model):
    username = models.EmailField(max_length=50)
    # email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    cpassword = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['username']
    
    
    
   
