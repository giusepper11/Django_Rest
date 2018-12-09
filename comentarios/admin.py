from django.contrib import admin

from comentarios.models import Comentario
from comentarios.actions import reprova_comentarios,aprova_comentarios

# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'aprovado')
    actions = (reprova_comentarios, aprova_comentarios)


admin.site.register(Comentario, ComentarioAdmin)
