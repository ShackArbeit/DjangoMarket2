from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
      name=models.CharField(max_length=200)

      class Meta:
        ordering = ('name',)
        verbose_name_plural = '產品種類'
      
      def __str__(self):
           return self.name

class Items(models.Model):
     name=models.CharField(max_length=200)
     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
     description=models.TextField(blank=True,null=True)
     price=models.FloatField()
     image=models.ImageField(upload_to='item_images',blank=True,null=True)
     is_sold=models.BooleanField(default=False)
     created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
     created_at=models.DateField(auto_now_add=True)
     def __str__(self):
        return self.name 

     class Meta:
        verbose_name_plural = '產品項目'
