from django.shortcuts import render
from django.http import HttpResponse
# from .models import Socio
# from .forms import SocioForm

# Create your views here.
def inicio(request):
    return render(request,'paginas_base/inicio.html')
#def lista(request):
 #   socios=Socio.object.all()
#  return render(request,'paginas_base/lista.html',{'socios':socios})