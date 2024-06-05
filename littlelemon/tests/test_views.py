from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from restaurant.views import MenuItemView

class MenuViewTest(TestCase):
    def setup(self):
        self.view = MenuItemView()
        self.m1 = Menu.objects.create(name = "Cookie", price = 3.00, inventory = 10)
        self.m2 = Menu.objects.create(name = "Milk", price = 1.00, inventory = 20)
    
    def test_getall(self):
        s_data = MenuItemSerializer(Menu.objects.all(), many=True).data
        
    