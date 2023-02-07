from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menuitem'),
    path('api-token-auth', obtain_auth_token),
    path('book', views.BookingViewSet.as_view({'post':'create'}), name='book'),
    path('bookings', views.BookingViewSet.as_view({'get': 'list'}), name='reservations'),
]

