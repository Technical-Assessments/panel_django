from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F

from datatable_null_vendors.models import DataTable
from rest_framework import viewsets
from datatable_null_vendors.serializers import TripSerializer
from datatable_null_vendors.models import Yellowtaxis

# Create your views here.


def home_view(request, *args, **kwargs):

    return render(request, "home.html")


def panel(request, *args, **kwargs):

    rows = DataTable.objects.all()
    paginator = Paginator(rows, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    '''
    data = DataTable.objects.all()
    paginator = Paginator(data, 100)
    page = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    page_obj = DataTable.objects.all()
    '''

    return render(request, "base.html", {'page_obj': page_obj})


def edit(request, id):
    row = DataTable.objects.get(id=id)
    return render(request, 'edit.html', {'row': row})


class TripViewSet(viewsets.ModelViewSet):
    queryset = Yellowtaxis.objects.all().order_by('vendorid'
        #F('trip_distance').desc(nulls_last=True)
    )
    serializer_class = TripSerializer
