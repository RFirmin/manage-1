from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Description")
    number = models.IntegerField(blank=True, default=0, verbose_name="Quantity_of_equipment")
    image = models.ImageField(upload_to='enter_image/', null=True, blank=True)

    class Meta:
        verbose_name = "Category_Equipment"

    def __str__(self):
        return self.title
    

class Equipment(models.Model):
    serial_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100, unique=True, verbose_name="Name_of_equipement")
    quantity = models.IntegerField(blank=True, default=1)
    procurement = models.CharField(max_length=100)
    cost = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True, verbose_name="update_equipement")
    created_on = models.DateField(auto_now=True, verbose_name="created_equipement")
    classed = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category_of_equipement")
    state = models.BooleanField(default=True)
    number = models.IntegerField()

    class Meta:
        verbose_name = "Equipment_stored"

    def __str__(self):
        return self.description
    
@receiver(pre_save, sender=Equipment)
def increment_number(sender, instance, **kwargs):
    if not instance.number:
        max_number = Equipment.objects.aggregate(models.Max('number'))['number__max']
        instance.number = (max_number or 0) + 1

    
