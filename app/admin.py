# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Corso,  Iscrizione, Aula, Approvazione, Comunicazione, Permessi


# Register your models here.
class IscrizioneAdmin(admin.ModelAdmin):
    list_display = ('user', 'corso1','corso2','corso3','corso4','corso5','corso6','corso7','corso8', 'corso9')
    search_fields = ['user__username']

class CorsiAdmin(admin.ModelAdmin):
    list_display = ( 'titolo','esperti_esterni','f1','f2','f3','f4','f5','f6','f7','f8', 'f9')
    search_fields = ['titolo', 'studente_referente1', 'studente_referente2', 'studente_referente3', 'studente_referente4', 'studente_referente5', 'esperti_esterni']

admin.site.register(Corso, CorsiAdmin)
admin.site.register(Aula)
admin.site.register(Iscrizione, IscrizioneAdmin)
admin.site.register(Approvazione)
admin.site.register(Comunicazione)
admin.site.register(Permessi)
