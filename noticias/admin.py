from django.contrib import admin
from noticias.models import Noticia, Rubrica

class RubricaAdmin(admin.ModelAdmin):
	list_display = ('title','slug',)
 
class NoticiaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Rubrica, RubricaAdmin)