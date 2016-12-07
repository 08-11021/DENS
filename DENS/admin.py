from django.contrib import admin

# these lines added:

from django.contrib import admin
from .models import Usuario

class ChoiceInline(admin.TabularInline):
    model = Usuario
    extra = 3

admin.site.register(Usuario)
