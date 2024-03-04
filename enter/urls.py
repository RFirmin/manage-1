from django.urls import path

from . import views

app_name = 'enter'

urlpatterns = [
    path('', views.screen_category, name='screen_category'),   
    path('add category/', views.add_category, name='add_category'),
    
    path('all equipments/', views.screen_equipment, name='screen_equipment'),   
    path('details equipment/<int:id>/', views.details_equipment, name='details_equipment'),
    path('add equipment/', views.add_equipment, name='add_equipment'),

    path('all equipments out/', views.screen_equipmentOut, name='screen_equipmentOut'),
    path('details equipment out/<int:id>/', views.details_equipmentOut, name='details_equipmentOut'),
    path('add equipment out/', views.add_equipmentOut, name='add_equipmentOut'),

    path('history/', views.screen_history, name='screen_history'),
    
    path('export json/', views.export_data_as_json, name='export_data_as_json'),
    path('export json number/<int:id>/', views.export_data_as_json_by_id, name='export_data_as_json_id'),
    path('export json text/', views.export_data_as_json_into_text, name='export_data_as_json_into_text'),
    
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