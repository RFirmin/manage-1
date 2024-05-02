import csv
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Equipment, Equipment_Out

@receiver(post_save, sender=Equipment)
def save_equipment_to_csv(sender, instance, created, **kwargs):
    # Nom du fichier CSV de sauvegarde
    csv_filename = 'store_manage/enter/data/equipment_backup.csv'

    # Vérifier si le fichier CSV existe déjà
    file_exists = os.path.isfile(csv_filename)

    # Extraire les données de l'instance nouvellement enregistrée
    data = [
        instance.serialNumber,
    ]

    # Écriture des données dans le fichier CSV
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(data)


@receiver(post_save, sender=Equipment_Out)
def remove_equipment(sender, instance, created, **kwargs):
    if created:
        serial_number = instance.serialNumber
        equipment = Equipment.objects.filter(serialNumber=serial_number).first()
        if equipment:
            equipment.delete()


@receiver(post_save, sender=Equipment_Out)
def update_Category_number(sender, instance, **kwargs):
    instance.classed.number -= 1
    instance.classed.save()


"""

       #instance.description,
        #instance.quantity,
        #instance.supplier,
        #instance.cost,
        #instance.last_update,
        #instance.created_on,
        #instance.classed,
        #instance.state,
        #instance.image.path if instance.image else ''
 
# Écrire l'en-tête du fichier CSV si c'est la première entrée
        if not file_exists:
            header = [
                'Serial Number',
                'Description',
                'Quantity',
                'Supplier',
                'Cost',
                'Last Update',
                'Created On',
                'Classed',
                'State',
                'Image Path'
            ]
            writer.writerow(header)

"""