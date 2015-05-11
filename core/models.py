# coding: utf-8
from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=70, verbose_name="Назва")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Type(models.Model):
    name = models.CharField(max_length=70, verbose_name="Назва")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Distinct(models.Model):
    name = models.CharField(max_length=70, verbose_name="Назва")
    region = models.ForeignKey(Region, verbose_name="Регіон")

    def __unicode__(self):
        return "%s >> %s" %(self.name, self.region.name)

    class Meta:
        verbose_name = 'Район'
        ordering = ['-id']


class City(models.Model):
    name = models.CharField(max_length=70, verbose_name="Назва")
    distinct = models.ForeignKey(Distinct, verbose_name='Район')

    def __unicode__(self):
        return "%s >> %s" %(self.name, self.distinct.name)

    class Meta:
        ordering = ['-id']


class Place(models.Model):
    name = models.CharField(max_length=70, verbose_name="Назва")
    city = models.ForeignKey(City, verbose_name='Місто')

    def __unicode__(self):
        return "%s >> %s" %(self.name, self.city.name)

    class Meta:
        ordering = ['-id']


class Marchent(models.Model):
    first_name = models.CharField(max_length=70, verbose_name="Ім`я")
    last_name = models.CharField(max_length=70, verbose_name='По-Батькові')
    sur_name = models.CharField(max_length=70, verbose_name='Прізвище')
    telephone = models.CharField(max_length=60, verbose_name='Телефон')
    email = models.EmailField(max_length=150, verbose_name='Email')
    city = models.ForeignKey(City, verbose_name='Місто')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    description = models.TextField(verbose_name='Додаткова інформація', blank=True)

    def __unicode__(self):
        return "%s %s.%s." % (self.sur_name, self.first_name[:1], self.last_name[:1])

    class Meta:
        ordering = ['-id']


class Owner(models.Model):
    first_name = models.CharField(max_length=70, verbose_name="Ім`я")
    last_name = models.CharField(max_length=70, verbose_name='По-Батькові')
    sur_name = models.CharField(max_length=70, verbose_name='Прізвище')
    telephone = models.CharField(max_length=60, verbose_name='Телефон')
    email = models.EmailField(max_length=150, verbose_name='Email')
    city = models.ForeignKey(City, verbose_name='Місто')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    description = models.TextField(verbose_name='Додаткова інформація', blank=True)

    def __unicode__(self):
        return "%s %s.%s." % (self.sur_name, self.first_name[:1], self.last_name[:1])

    class Meta:
        ordering = ['-id']


class Container(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    type = models.ForeignKey(Type, verbose_name='Тип')
    weight = models.IntegerField(verbose_name='Тоннаж')
    row = models.IntegerField(verbose_name='Ряд')
    place = models.ForeignKey(Place, verbose_name='Місце')
    marchent = models.ForeignKey(Marchent, verbose_name='Орендарь')
    rent = models.CharField(max_length=255, verbose_name='Оренда')
    owner = models.ForeignKey(Owner, verbose_name='Власник')
    contract_begin = models.DateField(verbose_name='Початок оренди')
    contract_end = models.DateField(verbose_name='Кінець оренди')
    description = models.TextField(verbose_name='Додаткова інформація', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']