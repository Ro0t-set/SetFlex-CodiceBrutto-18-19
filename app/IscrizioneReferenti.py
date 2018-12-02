from .models import Corso, Iscrizione, Approvazione
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
def iscrizioniReferenti(corso_id, utente):


    iscrizione= Iscrizione.objects.get(user=utente)
    print(iscrizione)
    # corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get(id=corso_id)
    print(fasca)
    # iscrizione=get_object_or_404(Iscrizione, pk=tabella)
    #
    #
    #
    if fasca.f1 and iscrizione.corso1_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f2 and iscrizione.corso2_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f3 and iscrizione.corso3_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f4 and iscrizione.corso4_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f5 and iscrizione.corso5_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f6 and iscrizione.corso6_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f7 and iscrizione.corso7_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f8 and iscrizione.corso8_id != None:
        messages.error(request, 'Fascia gia occupata!')

    if fasca.f9 and iscrizione.corso9_id != None:
        messages.error(request, 'Fascia gia occupata!')


    print("qui ci arrivo")

    if fasca.f1 and iscrizione.corso1_id== None:
        iscrizione.corso1 = fasca
        iscrizione.save()
    if fasca.f2 and iscrizione.corso2_id== None:
        iscrizione.corso2 = fasca
        iscrizione.save()
    if fasca.f3 and iscrizione.corso3_id== None:
        iscrizione.corso3= fasca
        iscrizione.save()
    if fasca.f4 and iscrizione.corso4_id== None:
        iscrizione.corso4= fasca
        iscrizione.save()
    if fasca.f5 and iscrizione.corso5_id== None:
        iscrizione.corso5= fasca
        iscrizione.save()
    if fasca.f6 and iscrizione.corso6_id== None:
        iscrizione.corso6= fasca
        iscrizione.save()
    if fasca.f7 and iscrizione.corso7_id== None:
        iscrizione.corso7= fasca
        iscrizione.save()
    if fasca.f8 and iscrizione.corso8_id== None:
        iscrizione.corso8= fasca
        iscrizione.save()
    if fasca.f9 and iscrizione.corso9_id== None:
        iscrizione.corso9= fasca
        iscrizione.save()
