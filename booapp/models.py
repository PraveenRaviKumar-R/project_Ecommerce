from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    stock=models.PositiveIntegerField(default=0)

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    added_at=models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.product.price * self.quantity
    
class Order(models.Model):
    STATUS_CHOICES=(('Pending','Pending'),('Processing','Processing'),
                    ('Shipped','Shipped'),('Delivered','Delivered'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(CartItem)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    name=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=20,default='')
    email=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Pending')
    ordered_at=models.DateTimeField(auto_now_add=True)


