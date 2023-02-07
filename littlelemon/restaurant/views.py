from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import render
from django.core import serializers
import json

from .models import Menu, Booking
from .forms import BookingForm
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservations(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def book(request):
    try:
        if request.method == 'POST':
            formData = json.load(request)
            db_entry = BookingForm(data=formData)
            if db_entry.is_valid():
                db_entry.save()
    except Exception as err:
        message = "Form data not accepted. Data needs to be in JSON format. Alternatively, enter data using the browsable web form."
        warning = {'error': str(err), 'message': message}
        return Response(warning, status=406)

    return render(request, 'book.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''    
    return render(request, 'menu_item.html', {'menu_item':menu_item})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

