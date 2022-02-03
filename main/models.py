from django.db import models
from django.core.validators import MinLengthValidator
from main.validators import only_letters_validator, file_max_size_in_mb_validator
import datetime

class Profile(models.Model):
    """
    Profile
        The user must provide the following information in their profile:
            • The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
            • The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
            • Profile picture - the user can link their picture using a URL.

        The user may provide the following information in their profile:
            • Date of birth: day, month, and year of birth.
            • Description - a user can write any description about themselves, no limit of words/chars.
            • Email - a user can only write a valid email address.
            • Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
    """
    # КАК ДОСТЪПВАМЕ ДИРЕКТНО ТАЗИ КОНСТАНТА , НЕ Е ЛИ НУЖЕН self.?? E taka
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(choice, choice) for choice in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            # creating object with this class (init)
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            # reference to function so Django could use it.
            only_letters_validator,
        ])
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ])
    image = models.URLField()

    # OPTIONAL, blank for administration forms, and forms to be empty ''
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    ########
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    """
    Pet
        The user must provide the following information when adding a pet in their profile:
            • Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
            • Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
        The user may provide the following information when adding a pet to their profile:
            • Date of birth - pet's day, month, and year of birth.
    """

    # CONTSTANTS
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    NAME_MAX_LENGTH = 30

    # FIELDS/COLUMNS
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )

    date_of_birth = models.DateField(null=True, blank=True)

    # ONE-TO-ONE RELATIONS
    #  ------
    # ONE-TO-MANY RELATIONS
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    #  MANY-TO-MANY RELATIONS
    #  ------

    # Properties
    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
    # Methods

    # Dunder methods

    # Meta
    class Meta:
        """
        See model docs
        • Name -  All pets' names should be unique for that user.
        """

        # OH FOR THIS USER THE PET NAME SHOULD BE UNIQUE ! THATS WHY
        # NOT ALLOWED SAME USER WITH SAME NAME
        # ONE USER HAVE UNIQUE PET NAMES,
        # Antoan can have Pesho pet i Gosho pet, no ne i Pesho pet i Pesho pet za Antoan
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    """
        Pet's Photo
    The user must provide the following information when uploading a pet's photo in their profile:
        • Photo - the maximum size of the photo can be 5MB
        • Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
    The user may provide the following information when uploading a pet's photo in their profile:
        • Description - a user can write any description about the picture, with no limit of words/chars
    Other:
        • Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
        • Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited.
    """

    photo = models.ImageField(
        validators=[file_max_size_in_mb_validator(5)]
    )
    # Edin pet moje da e v mnogo snimki, edna snimka moje da ima mnogo pets
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate atleast 1 pet
    )

    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    likes = models.IntegerField(default=0)
