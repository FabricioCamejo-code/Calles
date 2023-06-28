from django.contrib import admin

# Register your models here.
from .models import Pais, Ciudad, Calle, Voto, Comment, Visit

admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Calle)
admin.site.register(Voto)
admin.site.register(Comment)
admin.site.register(Visit)