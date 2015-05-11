# coding: utf-8
from django import forms
from django.contrib.admin import widgets

from core.models import Distinct, City, Place, Owner, Marchent, Container, Type, Region


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        exclude = []


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = []


class DistinctForm(forms.ModelForm):
    class Meta:
        model = Distinct
        fields = ['name', 'region']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'distinct']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'city']


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = []
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
        }


class MarchentForm(forms.ModelForm):
    class Meta:
        model = Marchent
        exclude = []
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
        }


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        exclude = []
        widgets = {
            'contract_begin': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'contract_end': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }
