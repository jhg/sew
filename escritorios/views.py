#from escritorios.models import Escritorio
from django.shortcuts import render_to_response

def escritorio(request):
    return render_to_response("escritorio.htm", {})
