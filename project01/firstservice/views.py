from django.shortcuts import render, get_object_or_404
from .models import chaiVariety

# Create your views here.
def all_chai(req):
    chais = chaiVariety.objects.all()
    return render(req, 'firstservice/anyname.html', {'data': chais})

def order(req):
    return render(req, 'firstservice/order.html')

def chai_detail(req, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(req, 'firstservice/chaiDetail.html', {'data' : chai})