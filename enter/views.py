from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Equipment, Equipment_Out, ActionHistory
from .forms import CategoryForm, EquipmentForm, EquipmentOutForm

from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.paginator import Paginator
from django.utils import timezone

from django.http import JsonResponse
import json

# Create your views here.

# View for the action to screen

@login_required
def screen_category(request):
    
    enter_category = Category.objects.all()

    context = {
        'equipments' : enter_category,
    }

    return render(request, "all_category.html", context)


@login_required
#@user_passes_test(lambda u: "master" in [group.name for group in u.groups.all()])
def screen_equipment(request):
    
    enter_equipment = Equipment.objects.all()

    paginator = Paginator(enter_equipment, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'equipments' : page_object,
    }

    return render(request, "all_equipment.html", context)


@login_required
#@user_passes_test(lambda u: "master" in [group.name for group in u.groups.all()])
def screen_equipmentOut(request):
    
    enter_equipmentOut = Equipment_Out.objects.all()

    paginator = Paginator(enter_equipmentOut, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'equipments' : page_object,
    }

    return render(request, "all_equipmentOut.html", context)


@login_required
def screen_history(request):
    
    enter_history = ActionHistory.objects.all()

    context = {
        'equipments' : enter_history,
    }

    return render(request, "history.html", context)



# View for the action to details

@login_required
def details_equipment(request, id):
    
    #details = Equipment.objects.get(number=number)
    details = get_object_or_404(Equipment, id=id)
    context = {
        'details' : details
    }
    
    return render(request, 'details_equipment.html', context)


@login_required
def details_equipmentOut(request, id):
    
    #details = Equipment.objects.get(number=number)
    details = get_object_or_404(Equipment_Out, id=id)
    context = {
        'details' : details
    }
    
    return render(request, 'details_equipmentOut.html', context)



# View for the action to add

@login_required
def add_category(request):
        
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            
            action = ActionHistory(user=request.user, action="input_category", timestamp=timezone.now())
            action.save()
            return redirect('enter:screen_category')
            
    else:
        form = CategoryForm()
        
    context = {
        'form': form,
    }

    return render(request, 'add_category.html', context)


@login_required
def add_equipment(request):
        
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()

            action = ActionHistory(user=request.user, action="input_equipment", timestamp=timezone.now())
            action.save()
            
            return redirect('enter:screen_category')
   
    else:
        form = EquipmentForm()
        
    context = {
        'form': form,
    }
    return render(request, 'add_equipment.html', context)


@login_required
def add_equipmentOut(request):
        
    if request.method == 'POST':
        form = EquipmentOutForm(request.POST)
        if form.is_valid():
            form.save()

            action = ActionHistory(user=request.user, action="output_equipment", timestamp=timezone.now())
            action.save()
            
            return redirect('enter:screen_category')
   
    else:
        form = EquipmentOutForm()
        
    context = {
        'form': form,
    }
    return render(request, 'add_equipmentOut.html', context)

"""
@login_required
def add_equipmentOut(request):
        
    if request.method == 'POST':
        form = EquipmentOutForm(request.POST)
        if form.is_valid():
            form.save()

            action = ActionHistory(user=request.user, action="output_equipment", timestamp=timezone.now())
            action.save()
            
            return redirect('enter:screen_category')
   
    else:
        form = EquipmentOutForm()
        
    context = {
        'form': form,
    }
    return render(request, 'add_equipmentOut.html', context)
"""


# view for json

def export_data_as_json(request):
    data = list(Equipment.objects.values())
    return JsonResponse(data, safe=False)
 
def export_data_as_json_by_id(request, id):
    data = Equipment.objects.values('serialNumber', 'description', 'procurement', 'cost', 'created_on', 'state',).get(id=id)
    return JsonResponse(data, safe=False)

def export_data_as_json_into_text(request):
    data = list(Equipment.objects.values())
    with open('dataEquipmentlist.json', 'w') as file:
        json.dump(data, file)
    return JsonResponse({'message': 'Ok'})



# view for graphic

@login_required
def state(request):
    
    graph_category = Category.objects.all()

    context = {
        'equipments' : graph_category,
    }

    return render(request, "graph_category.html", context)



#

"""
@login_required
def get_equipment(request):
    if request.method == "POST":
        form = EquipmentOutForm(request.POST)
        if form.is_valid():
            form.save(using='database2')
            print(form.classed)
            print(form.serialNumber)

            action = ActionHistory(user=request.user, action="output_equipment", timestamp=timezone.now())
            action.save()
            
            return redirect('enter:screen_category')
        
        else:
            print(form.errors)
    else:
        form = EquipmentOutForm()

    context = {
        'form': form,
    }

    return render(request, 'add_equipmentOut.html', context)


@login_required
def load_equipments(request):
    classed_id = request.GET.get("classed")
    print(classed_id)
    equipments = Equipment_Out.objects.filter(classed_id=classed_id)
    print(equipments)
    
    context = {
        'equipments' : equipments
    }
    return render(request, 'serie_options.html', context)
""" 