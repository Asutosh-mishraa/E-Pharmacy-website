from django.db import models
from user.models import MyUser


# Create your models here.
class category(models.Model):
    category=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.category
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    secondary_description=models.TextField(blank=True)
    is_available=models.BooleanField(default=True)
    prescription_required=models.BooleanField(default=False)
    product_image=models.ImageField(upload_to="prod_images/")

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    order_details=models.CharField(max_length=500)
    total_price=models.FloatField()
    payment_mode = models.TextField()
    is_paid = models.BooleanField(default=False)
    is_delivered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username