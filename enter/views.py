from django.shortcuts import render, redirect

from .models import Category, Equipment

from .forms import CategoryForm, EquipmentForm

from django.core.paginator import Paginator

# Create your views here.

def screen_category(request):
    
    enter_category = Category.objects.all()

    context = {

    }

    return render(request, "all_category.html", context)


def screen_equipment(request):
    
    enter_equipment = Equipment.objects.all()

    paginator = Paginator(enter_equipment, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {

    }

    return render(request, "all_equipment.html", context)

