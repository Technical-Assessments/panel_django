from django import forms
from datatable_null_vendors.models import DataTable


class VendorForm(forms.ModelForm):
    class Meta:
        model = DataTable
        fields = ['vendorid', 'tpep_pickup_datetime', 'trip_distance',
                  'payment_type']  # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        '''
        widgets = {'vendorid': forms.TextInput(attrs={'class': 'form-control'}),
                   'tpep_pickup_date': forms.EmailInput(attrs={'class': 'form-control'}),
                   'trip_distance': forms.EmailInput(attrs={'class': 'form-control'}),
                   'payment_type': forms.EmailInput(attrs={'class': 'form-control'})
                   }
        
        widgets = {'vendorid': forms.FloatField(),
                   'tpep_pickup_date': forms.DateTimeField(),
                   'trip_distance': forms.FloatField(),
                   'payment_type': forms.FloatField()
                   }
        '''
        widgets = {'vendorid': forms.NumberInput(attrs={'class': 'form-control'}),
                   'tpep_pickup_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'trip_distance': forms.NumberInput(attrs={'class': 'form-control'}),
                   'payment_type': forms.NumberInput(attrs={'class': 'form-control'})
                   }
