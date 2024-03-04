from django.test import TestCase
from .models import Category, Equipment
# Create your tests here.

class TestCaseCategory(TestCase):

    def setUp(self):
        
        self.data = {
            'title': '',
            'slug': '',
            'description': '',
            'number': '',
            'image': ''
        }

        self.category = Category.objects.create_category(**self.data)

        self.equipment = Equipment.objects.create(
            category=self.category
        )

    def test_category_can_speak(self):
        """Category that can speak are correctly identified"""
        lion = Category.objects.get(title="lion")
        cat = Category.objects.get(title="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
    