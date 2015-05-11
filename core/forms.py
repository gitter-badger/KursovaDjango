# coding: utf-8
from django import forms

from core.models import Distinct, City, Place, Owner, Marchent, Container


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


class MarchentForm(forms.ModelForm):
    class Meta:
        model = Marchent
        exclude = []


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        exclude = []