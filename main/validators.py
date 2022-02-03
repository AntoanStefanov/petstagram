from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Value must contain only letters')


def file_max_size_in_mb_validator(max_size):
    # https://stackoverflow.com/questions/1875316/validate-image-size-in-django-admin
    def validate(image):
        # -2:20 min in video
        filesize = image.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError('Max file size in %sMB' % str(max_size))
    return validate
