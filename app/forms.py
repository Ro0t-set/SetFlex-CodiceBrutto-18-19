from django import forms
from django.db import models
from django.forms import formset_factory
from django.utils import timezone
import re
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Corso, Iscrizione, Approvazione



class CreaCorsi(forms.ModelForm, forms.Form):
    referente1 = forms.CharField(label='referente1', max_length="100", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    referente2 = forms.CharField(required = False,label='referente2', max_length="100", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    referente3 = forms.CharField(required = False,label='referente3', max_length="100", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    referente4 = forms.CharField(required = False,label='referente4', max_length="100", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    referente5 = forms.CharField(required = False,label='referente5', max_length="100", widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    class Meta:
        model = Corso
        fields = ['titolo','esperti_esterni','classi_autori', 'descrizione','aule', 'progressivo','f1','f2','f3','f4','f5','f6','f7','f8','f9' ]
        widgets = {
            'titolo': forms.TextInput(attrs={'class': 'form-control'}),
            #'studenti_referenti': forms.TextInput(attrs={'class': 'form-control'}),
            'classi_autori': forms.TextInput(attrs={'class': 'form-control'}),
            'esperti_esterni': forms.TextInput(attrs={'class': 'form-control'}),
            'descrizione': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),

        }

class ConvalidaCorsi(forms.ModelForm):
    class Meta:
        model = Approvazione
        fields = ['convalida']


class IscrizioneForm(forms.ModelForm):
    class Meta:
        model = Iscrizione
        fields = ['corso1', 'corso2', 'corso3', 'corso4', 'corso5', 'corso6', 'corso7', 'corso8', 'corso9']


class Mail(forms.Form):
    testo=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows':'3' }))
    mail= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

class CercaCorsi(forms.Form):
    q = forms.CharField(label='nome', max_length="100")
