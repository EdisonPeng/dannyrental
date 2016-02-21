from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Home, HomePhoto, Room, RoomPhoto, About, Transportation, Reservation, ContactInfo

def index(request):
    home = get_object_or_404(Home, pk=1)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'home': home, 'contact_info': contact_info}
    return render(request, "rental/index.html", context)

def about(request):
    abouts = get_list_or_404(About)
    transportation_list = get_list_or_404(Transportation)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'abouts': abouts, 'transportation_list': transportation_list, 'contact_info': contact_info}
    return render(request, "rental/about.html", context)

def rooms(request):
    rooms = get_list_or_404(Room)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'rooms': rooms, 'contact_info': contact_info}
    return render(request, "rental/rooms.html", context)

def reservation(request):
    reservations = get_list_or_404(Reservation)
    contact_info = get_object_or_404(ContactInfo, pk=1)
    context = {'reservations': reservations, 'contact_info': contact_info}
    return render(request, "rental/reservation.html", context)
