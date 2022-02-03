from django.shortcuts import render
from main.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets = profile.pet_set.all()
    context = {
        'pets': pets
        }

    return render(request, 'dashboard.html', context)


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request):
    return render(request, 'photo_details.html')
