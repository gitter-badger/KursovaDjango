# coding: utf-8
from django import forms

from core.models import Distinct, City, Place, Owner, Marchent, Container


class DistinctForm(forms.ModelForm):
    class Meta:
        model = Distinct


class CityForm(forms.ModelForm):
    class Meta:
        model = City


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner


class MarchentForm(forms.ModelForm):
    class Meta:
        model = Marchent


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container