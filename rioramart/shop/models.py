from django.db import models
from accounts.models import CustomUser


# Create your models here.

#Table category
class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category/')
    sort = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('sort', )
    
#Table for the product
class Product(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    rating = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    package_quantity = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    net_quantity = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-id', )


#Basket table
class Cart(models.Model):
    session_key = models.CharField(max_length=40)
    
    def __str__(self):
        return self.session_key
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.product} ({self.quantity})'


#Ordering table
class Order(models.Model):
    #Billing
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    billing_address_line1 = models.CharField(max_length=255)
    billing_address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    #Shopping
    shopping_first_name = models.CharField(max_length=100, blank=True)
    shopping_last_name = models.CharField(max_length=100, blank=True)
    shopping_email = models.EmailField()   
    shopping_phone = models.CharField(max_length=20, blank=True)
    
    shopping_company = models.CharField(max_length=100)
    shopping_address = models.CharField(max_length=255, blank=True)
    shopping_address_line1 = models.CharField(max_length=100)
    shopping_address_line2 = models.CharField(max_length=100, blank=True)
    shopping_city = models.CharField(max_length=100, blank=True)
    shopping_state = models.CharField(max_length=100, blank=True)
    shopping_zip_code = models.CharField(max_length=20, blank=True)
    shopping_country = models.CharField(max_length=100, blank=True)
    
    #payment_method = models.CharField(max_length=30)
    #total_price = models.DecimalField(max_digits=10, decimal_places=2)
    #status = models.CharField(max_length=20, default="pending")
    #updated_at = models.DateTimeField(auto_now=True)
    #shipping_same_as_billing = models.BooleanField(default=True)
    
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name}-{self.last_name}'
    
    class Meta:
        verbose_name_plural = 'orders'
        ordering = ('-created_at', )
    
#Table Reviews
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ('created_at', )
        
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)