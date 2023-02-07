from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth', obtain_auth_token),
    path('', views.index, name='index'),
    # path('menu', views.MenuItemView.as_view(), name='menu'),
    # path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menuitem'),
    # path('book/', views.BookingViewSet.as_view({
    #     'post':'create',
    #     'get': 'list',
    #     }), name="book"),
    path('about', views.about, name="about"),
    path('menu', views.menu, name='menu'),
    path('menu/<int:pk>', views.display_menu_items, name='menu_item'),
    path('book', views.book, name="book"),
    path('bookings', views.reservations, name='bookings'),
]

