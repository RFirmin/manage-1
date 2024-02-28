from django.db import models
from django.contrib.auth.models import User

#from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    number = models.IntegerField(blank=True, default=0, verbose_name="Quantity_of_equipment")
    image = models.ImageField(upload_to='enter_category/', blank=True, null=True)

    class Meta:
        verbose_name = "Category_Equipment"

    def __str__(self):
        return self.title
    

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    serialNumber = models.CharField(max_length=100)
    description = models.CharField(max_length=100, unique=False, verbose_name="Name_of_equipment")
    quantity = models.IntegerField(blank=True, default=1)
    supplier = models.CharField(max_length=100)
    cost = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True, verbose_name="update_equipment")
    created_on = models.DateField(auto_now_add=True, verbose_name="created_equipment")
    classed = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category_of_equipment")
    state = models.BooleanField(default=True)
    image = models.ImageField(upload_to='enter_equipment/', blank=True, null=True)

    class Meta:
        verbose_name = "Equipment stored"

    def __str__(self):
        return self.description
    

class Equipment_Out(models.Model):
    id = models.AutoField(primary_key=True)
    serialNumber = models.CharField(max_length=100)
    description = models.CharField(max_length=100, unique=False, verbose_name="Name_of_equipment")
    projet = models.CharField(max_length=100, unique=False, verbose_name="Projet_of_equipment")
    quantity = models.IntegerField(blank=True, default=1)
    last_update = models.DateTimeField(auto_now=True, verbose_name="update_equipment")
    created_on = models.DateField(auto_now=True, verbose_name="created_equipment")
    classed = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category_of_equipment")
    equipment_in = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="equipment_in_stock")
    image = models.ImageField(upload_to='enter_equipmentOut/', blank=True, null=True)

    class Meta:
        verbose_name = "Equipment_Out"

    def __str__(self):
        return self.description
    
@receiver(post_save, sender=Equipment)
def update_Category_number(sender, instance, **kwargs):
    instance.classed.number += 1
    instance.classed.save()

class ActionHistory(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    action = models.CharField(max_length=100) 
    timestamp = models.DateField(auto_now=True, verbose_name="created_equipement")

    class Meta:
        verbose_name = "History"

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"

    
