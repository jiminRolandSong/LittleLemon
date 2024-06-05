from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Lemonade", price = 9.00, inventory=50)
        self.assertEqual(str(item), "Lemonade : 9.00")