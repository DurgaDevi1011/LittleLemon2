
from django.test import TestCase
from restaurant.models import Booking, Menu


class MenuItwmTestCase(TestCase):
    def test_menu_item(self):
        item = Menu.objects.create(tittle='Burger', price=100.00, inventory=10)
        self.assertEqual(item.tittle, 'Burger')
        self.assertEqual(item.price, 100.00)
        self.assertEqual(item.inventory, 10)
