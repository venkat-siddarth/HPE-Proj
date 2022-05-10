from django.db import models

# Create your models here.
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
class cart(models.Model):
    username=models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.username

class Product(models.Model):
    _id=models.IntegerField(default=0)
    username = models.ForeignKey(
        cart, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    get_absolute_url=models.CharField(max_length=255)
    get_image=models.CharField(max_length=255)
    get_thumbnail=models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=1)

    class Meta:
        ordering = ('date_added',)

    
