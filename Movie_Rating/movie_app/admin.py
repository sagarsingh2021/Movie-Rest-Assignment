from django.contrib import admin
from .models import  Genre, Actor, Director, Producer
# Register your models here.

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
