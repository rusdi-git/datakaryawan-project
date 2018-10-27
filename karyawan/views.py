from django.shortcuts import render

from .models import Karyawan
# Create your views here.
def home(request):
    return render(request, 'home.html')

def list_karyawan(request):
    karyawan = Karyawan.objects.all()
    return render(request, 'karyawan/listkaryawan.html', {'karyawan':karyawan})