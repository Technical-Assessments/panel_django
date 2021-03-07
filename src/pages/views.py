from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from datatable_null_vendors.models import DataTable
# Create your views here.


def home_view(*args, **kwargs):

    return HttpResponse("<h1> Hello </h1>")


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
