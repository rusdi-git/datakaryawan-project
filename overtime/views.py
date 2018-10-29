from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .engine import ATR_Processor
from .models import Overtime
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

def process_atr(request):
    atr_process = ATR_Processor()
    list = atr_process.openfile()
    atr_process.processfile(list)
    data_atr = atr_process.list_finger
    data_atr1 = []

    for d in data_atr:
        a = Overtime(noreg=d['id'], date_in=d['date_in'], date_out=d['date_out'])
        data_atr1.append(a)

    Overtime.objects.bulk_create(data_atr1)
    return render(request,'overtime/processatr.html', {'message':'ATR Successfully processed'})