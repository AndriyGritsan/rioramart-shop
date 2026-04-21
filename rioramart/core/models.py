from django.db import models

# Create your models here.

#Table contact
class Contact(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    number_phone1 = models.CharField(max_length=20)
    number_phone2 = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    email1 = models.EmailField()
    email2 = models.EmailField()
    description = models.TextField()
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    x = models.URLField(blank=True) 
    

#Table Message users
class MessageUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.DateField(auto_now=True)
    
    
#Table Subscription
class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default="Shop now")
    link = models.CharField(max_length=255, default="/shop/")
    type = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title