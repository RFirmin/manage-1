from django.shortcuts import render, redirect

from .models import Category, Equipment

from .forms import CategoryForm, EquipmentForm

from django.contrib.auth.decorators import user_passes_test

from django.core.paginator import Paginator

# Create your views here.

def screen_category(request):
    
    enter_category = Category.objects.all()

    context = {
        'equipments' : enter_category,
    }

    return render(request, "all_category.html", context)


@user_passes_test(lambda u: "master" in [group.name for group in u.groups.all()])
def screen_equipment(request):
    
    enter_equipment = Equipment.objects.all()

    paginator = Paginator(enter_equipment, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'equipments' : page_object,
    }

    return render(request, "all_equipment.html", context)


def details_equipment(request, serial_number):
    
    details = Equipment.objects.get(number=serial_number)
    
    context = {
        'details' : details
    }
    
    return render(request, 'details_equipment.html', context)