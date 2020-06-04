from django.shortcuts import render
from .models import Item

# Create your views here.


def get_mp_list(request):
    results = Item.objects.all()
    return render(request, "mp_list.html", {'items': results})
