from django.urls import path

from . import views

app_name = 'storage'

urlpatterns = [
    path('all equipments/', views.screen_equipment, name='print_equipments'),   
    path('all category/', views.screen_category, name='print_category'),   
    path('details equipment-<str:equipment_serial_number>/', views.details_equipment, name='details_equipment'),
    #path('new equipment/', views.new_equipment, name='new_equipment'),
    #path('new element/', views.new_element, name='new_element'),
    #path('update element/<int:id>/', views.update_element, name='update_element'),
    #path('choice element/', views.choice_element, name='choice_element'),
    #path('update equipment/<int:id>/', views.update_equipment, name='update_equipment'), 
    #path('delete equipment/<int:id>/', views.delete_equipment, name='delete_equipment'), 
    #path('', views.get_equipment, name='get_equipment'),
    #path('load serie/', views.load_serie, name='load_serie'),
    #path('graphic/', views.graphic, name='graphic'),
    #path('routeur/', views.routeur, name='routeur'), 
    #path('state/', views.state, name='state'),
    #path('routeur/', views.routeur, name='routeur'), 
    #path('new routeur/', views.new_routeur, name='new_routeur'),
    #path('search equipment/', views.search_equipment, name='search_equipment'), 
]