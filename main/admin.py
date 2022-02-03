from django.contrib import admin
from main.models import Profile, Pet, PetPhoto
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Pet

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [PetInlineAdmin]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
