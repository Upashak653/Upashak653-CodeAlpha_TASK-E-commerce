from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField(null=True)

    def __str__(self):
        return self.User_name
    

class Order(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField(null=True)
    Email = models.EmailField(null=True)
    Order = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.Name