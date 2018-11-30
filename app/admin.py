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
    search_fields = ['titolo', 'studente_referente1__username', 'studente_referente2__username', 'studente_referente3__username', 'studente_referente4__username', 'studente_referente5__username', 'esperti_esterni']


class ApprovazioneAdmin(admin.ModelAdmin):
    list_display = ( 'corso','alunno','convalida')
    search_fields = ['corso__titolo','alunno__username']


admin.site.register(Corso, CorsiAdmin)
admin.site.register(Aula)
admin.site.register(Iscrizione, IscrizioneAdmin)
admin.site.register(Approvazione, ApprovazioneAdmin)
admin.site.register(Comunicazione)
admin.site.register(Permessi)
