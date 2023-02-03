import json
from django.test import Client, TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

#TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=20, inventory=10)
        Menu.objects.create(title="Chocolate Cake", price=30, inventory=15)
        Menu.objects.create(title="Lemon Pie", price=40, inventory=8)        

    def test_getall(self):
        # expected_response = [
        #     {"id":2,"title":"IceCream","price":"20.00","inventory":10},
        #     {"id":3,"title":"Chocolate Cake","price":"30.00","inventory":15},
        #     {"id":4,"title":"Lemon Pie","price":"40.00","inventory":8}
        #     ]
        c = Client()
        response = c.get('/restaurant/menu') # MenuItemView.as_view()
        response_obj = json.loads(response.content)
        items = Menu.objects.all()
        serialized_obj = MenuItemSerializer(items, many=True).data
        self.assertEqual(response_obj, serialized_obj)
        