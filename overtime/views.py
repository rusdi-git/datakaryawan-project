from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def input_atr(request):
    if request.method == 'POST' and request.FILES['atrfile']:
        atrfile = request.FILES['atrfile']
        fs = FileSystemStorage()
        filename = fs.save(atrfile.name, atrfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'overtime/inputatr.html', {'uploaded_file_url':uploaded_file_url})
    else:
        return render(request, 'overtime/inputatr.html')