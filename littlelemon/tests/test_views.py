import json
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User

# TestCase class
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
        response = self.client.get('/restaurant/api-menu') # MenuItemView.as_view()
        response_obj = json.loads(response.content)
        items = Menu.objects.all()
        serialized_obj = MenuItemSerializer(items, many=True).data
        self.assertEqual(response_obj, serialized_obj)

class BookViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.formdata = u'''{
            "name": "Minnie Mouse",
            "no_of_guests": 2,
            "bookingDate": "2023-02-07T13:00"}'''

    def test_non_authorization(self):
        # No login and authentication
        response = self.client.get('/restaurant/bookings') # views.reservations
        self.assertEqual(response.status_code, 401)

    def test_401(self):
        # No login and authentication
        json_data = json.loads(self.formdata)
        response = self.client.post('/restaurant/book', json_data, content_type='application/json')  # views.book
        self.assertEqual(response.status_code, 401)
    
    def test_authorization(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/restaurant/bookings') # views.reservations
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200(self):
        self.client.force_login(user=self.user)
        json_data = json.loads(self.formdata)
        response = self.client.post('/restaurant/book', json_data, content_type='application/json')  # views.book
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_406(self):
        self.client.force_login(user=self.user)
        response = self.client.post('/restaurant/book', "test", content_type='application/json')  # views.book
        self.client.logout()
        self.assertEqual(response.status_code, 406)

