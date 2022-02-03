from django.contrib import admin
from main.models import Profile, Pet, PetPhoto
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
