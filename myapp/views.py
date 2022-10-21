from django.shortcuts import render
from .models import Polling
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import redirect
# Create your views here.


def index(request):
    if request.method == "POST":
        nama = request.POST.get("nama", "")
        tahun = request.POST.get("tahun", "")

        data = Polling(nama=nama, tahun=tahun)
        data.save()
    poling = Polling.objects.filter(tahun=2020)
    poling2 = Polling.objects.filter(tahun=2021)
    poling3 = Polling.objects.filter(tahun=2022)
    poling4 = Polling.objects.all()
    total = ["nama", "tahun"]
    total2 = ["nama2", "tahun2"]
    total3 = ["nama3", "tahun3"]
    context = {
        'poling': poling, 'poling2': poling2, 'poling3': poling3, 'poling4': poling4, 'total':total, 'total2':total2, 'total3':total3
    }
    return render(request, 'polling/index.html', context)

def delete(request,id):
    delete_poling = Polling.objects.get(id=id)
    delete_poling .delete()
    return HttpResponseRedirect('/')