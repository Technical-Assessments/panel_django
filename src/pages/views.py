from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import F
from rest_framework import generics

from datatable_null_vendors.models import DataTable, Yellowtaxis
from rest_framework import viewsets
from datatable_null_vendors.serializers import TripSerializer
from datatable_null_vendors.forms import VendorForm

# Create your views here.


def home_view(request, *args, **kwargs):

    return render(request, "home.html")


def panel(request, *args, **kwargs):

    # rows = DataTable.objects.all()
    # rows = DataTable.objects.get_queryset().order_by('id')
    rows = Yellowtaxis.objects.get_queryset().order_by('id')
    paginator = Paginator(rows, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "base.html", {'page_obj': page_obj})


def edit(request, id):
    row = DataTable.objects.get(id=id)
    return render(request, 'edit.html', {'row': row})


class TripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Yellowtaxis.objects.all().order_by('vendorid')
    serializer_class = TripSerializer


def update(request, id):
    row = DataTable.objects.get(id=id)
    form = VendorForm(request.POST, instance = row)
    if form.is_valid():
        form.save()
        return redirect("/")
    print("form is not valid")
    return render(request, 'edit.html', {'row': row})