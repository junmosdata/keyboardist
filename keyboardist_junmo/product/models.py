from django.db import models
from django.urls import reverse

from product.fields import ThumbnailImageField
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('UploadDate', auto_now_add=True)
    content = models.TextField('Product Description', default="default")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        ordering = ('upload_dt',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product:product_detail', args=(self.id,))
    