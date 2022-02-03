from django.shortcuts import render
from main.models import Profile

def show_home(request):
    context = {
        'profile': Profile.objects.all()
    }
    return render(request, 'home_page.html')


def show_dashboard(request):
    return render(request, 'dashboard.html')


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request):
    return render(request, 'photo_details.html')
