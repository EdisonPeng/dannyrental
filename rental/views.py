from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Home, HomePhoto, Room, RoomPhoto, About, Transportation, Reservation, ContactInfo

def index(request):
    home = get_object_or_404(Home, pk=1)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'home': home, 'contact_info': contact_info}
    return render(request, "rental/index.html", context)

def about(request):
    about = get_object_or_404(About, pk=1)
    transportation_list = get_list_or_404(Transportation)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'about': about, 'transportation_list': transportation_list, 'contact_info': contact_info}
    return render(request, "rental/about.html", context)

def rooms(request):
    rooms = Room.objects.all()
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'rooms': rooms, 'contact_info': contact_info}
    return render(request, "rental/rooms.html", context)

def reservation(request):
    reservation = get_object_or_404(Reservation, pk=1)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'reservation': reservation, 'contact_info': contact_info}
    return render(request, "rental/reservation.html", context)
