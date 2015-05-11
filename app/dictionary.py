# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from core.forms import DistinctForm, CityForm, PlaceForm, OwnerForm, MarchentForm, ContainerForm
from core.models import Region, Distinct, City, Place, Owner, Marchent, Container, Type


@login_required(login_url='/login')
def containers(request):
    list = Container.objects.all()
    return render_to_response('containers.html', locals())


@login_required(login_url='/login')
def regions(request):
    region = Region.objects.all()
    return render_to_response('regions.html', locals())


@login_required(login_url='/login')
def disctincts(request):
    list = Distinct.objects.all()
    return render_to_response('disctincts.html', locals())


@login_required(login_url='/login')
def cities(request):
    list = City.objects.all()
    return render_to_response('cities.html', locals())


@login_required(login_url='/login')
def places(request):
    list = Place.objects.all()
    return render_to_response('places.html', locals())


@login_required(login_url='/login')
def owners(request):
    list = Owner.objects.all()
    return render_to_response('owners.html', locals())


@login_required(login_url='/login')
def marchents(request):
    list = Marchent.objects.all()
    return render_to_response('marchents.html', locals())


@login_required(login_url='/login')
def region(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['region'] = Region.objects.get(id=int(request.GET.get('id')))
            return render_to_response('ajax/edit_region.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        return render_to_response('ajax/add_region.html', args)

    elif request.GET.get('action') == 'update':
        reg = Region.objects.get(id=int(request.GET.get('id')))
        reg.name = request.POST.get('name')
        reg.save()
        return HttpResponseRedirect('/dictionary/regions')

    elif request.GET.get('action') == 'remove':
        try:
            reg = Region.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/regions')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        Region.objects.create(name=request.POST.get('name'))
        return HttpResponseRedirect('/dictionary/regions')


@login_required(login_url='/login')
def distinct(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['distinct'] = Distinct.objects.get(id=int(request.GET.get('id')))
            args['regions'] = Region.objects.all()

            return render_to_response('ajax/disctinct.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = DistinctForm()
        args['form'] = form
        return render_to_response('ajax/disctinct.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            reg = Distinct.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/distincts')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = DistinctForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/disctinct.html', args)

        return HttpResponseRedirect('/dictionary/distincts')

    elif request.GET.get('action') == 'update':
        distinct = Distinct.objects.get(id=int(request.GET.get('id')))
        if request.POST:
            form = DistinctForm(request.POST)

            if form.is_valid():
                distinct.name = request.POST.get('name')
                distinct.region = Region.objects.get(id=int(request.POST.get('region')))
                distinct.save()
            else:
                args['distinct'] = Distinct.objects.get(id=int(request.GET.get('id')))
                args['regions'] = Region.objects.all()
                args['form'] = form
                return render_to_response('ajax/disctinct.html', args)

        return HttpResponseRedirect('/dictionary/distinct?action=edit&id='+str(distinct.id))


@login_required(login_url='/login')
def city(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['city'] = City.objects.get(id=int(request.GET.get('id')))
            args['distincts'] = Distinct.objects.all().only('id', 'name')
            return render_to_response('ajax/city.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = CityForm()
        args['form'] = form
        return render_to_response('ajax/city.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            reg = City.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/cities')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = CityForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/city.html', args)

        return HttpResponseRedirect('/dictionary/cities')

    elif request.GET.get('action') == 'update':
        city = City.objects.get(id=int(request.GET.get('id')))
        if request.POST:
            form = CityForm(request.POST)

            if form.is_valid():
                city.name = request.POST.get('name')
                city.distinct = Distinct.objects.get(id=int(request.POST.get('distinct')))
                city.save()
            else:
                args['city'] = City.objects.get(id=int(request.GET.get('id')))
                args['distincts'] = Distinct.objects.all()
                args['form'] = form
                return render_to_response('ajax/city.html', args)

        return HttpResponseRedirect('/dictionary/city?action=edit&id='+str(city.id))


@login_required(login_url='/login')
def place(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            data = Distinct.objects.get(id=int(request.GET.get('id')))
            form = DistinctForm({
                'id': data.id,
                'name': data.name,
                'region': data.region.id
            })

            args['form'] = form
            args['edit'] = True
            return render_to_response('ajax/city.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = PlaceForm()
        args['form'] = form
        return render_to_response('ajax/place.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            reg = Place.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/places')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = PlaceForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/place.html', args)

        return HttpResponseRedirect('/dictionary/places')


@login_required(login_url='/login')
def owner(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['owner'] = Owner.objects.get(id=int(request.GET.get('id')))
            args['cities'] = City.objects.all().only('id', 'name')
            args['edit'] = True
            return render_to_response('ajax/owner.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = OwnerForm()
        args['form'] = form
        return render_to_response('ajax/owner.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            reg = Owner.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/owners')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = OwnerForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/owner.html', args)

        return HttpResponseRedirect('/dictionary/owners')

    elif request.GET.get('action') == 'update':
        owner = Owner.objects.get(id=int(request.GET.get('id')))
        if request.POST:
            form = OwnerForm(request.POST)

            if form.is_valid():
                owner.first_name = request.POST.get('first_name')
                owner.last_name = request.POST.get('last_name')
                owner.sur_name = request.POST.get('sur_name')
                owner.email = request.POST.get('email')
                owner.telephone = request.POST.get('telephone')
                owner.city = City.objects.get(id=int(request.POST.get('city')))
                owner.address = request.POST.get('address')
                owner.description = request.POST.get('description')
                owner.save()
            else:
                args['form'] = form
                args['owner'] = owner
                return render_to_response('ajax/owner.html', args)

            return HttpResponseRedirect('/dictionary/owners')


@login_required(login_url='/login')
def marchent(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['marchent'] = Marchent.objects.get(id=int(request.GET.get('id')))
            args['cities'] = City.objects.all().only('id', 'name')
            return render_to_response('ajax/marchent.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = MarchentForm()
        args['form'] = form
        return render_to_response('ajax/marchent.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            reg = Marchent.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/dictionary/marchents')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = MarchentForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/marchent.html', args)

        return HttpResponseRedirect('/dictionary/marchents')

    elif request.GET.get('action') == 'update':
        marchent = Marchent.objects.get(id=int(request.GET.get('id')))
        if request.POST:
            form = MarchentForm(request.POST)

            if form.is_valid():
                marchent.first_name = request.POST.get('first_name')
                marchent.last_name = request.POST.get('last_name')
                marchent.sur_name = request.POST.get('sur_name')
                marchent.email = request.POST.get('email')
                marchent.telephone = request.POST.get('telephone')
                marchent.city = City.objects.get(id=int(request.POST.get('city')))
                marchent.address = request.POST.get('address')
                marchent.description = request.POST.get('description')
                marchent.save()
            else:
                args['form'] = form
                args['marchent'] = marchent
                return render_to_response('ajax/marchent.html', args)

            return HttpResponseRedirect('/dictionary/marchents')


@login_required(login_url='/login')
def container(request):
    args = {}
    args.update(csrf(request))

    if request.GET.get('action') == 'edit':
        try:
            args['container'] = Container.objects.get(id=int(request.GET.get('id')))
            args['types'] = Type.objects.all().only('id', 'name')
            args['owners'] = Owner.objects.all().only('id', 'first_name', 'last_name', 'sur_name')
            args['marchents'] = Marchent.objects.all().only('id', 'first_name', 'last_name', 'sur_name')
            args['places'] = Place.objects.all().only('id', 'name')
            return render_to_response('ajax/container.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'add':
        form = ContainerForm()
        args['form'] = form
        return render_to_response('ajax/container.html', args)

    elif request.GET.get('action') == 'remove':
        try:
            Container.objects.get(id=int(request.GET.get('id'))).delete()
            return HttpResponseRedirect('/')
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            form = ContainerForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                args['form'] = form
                return render_to_response('ajax/container.html', args)

        return HttpResponseRedirect('/')

    elif request.GET.get('action') == 'update':
        container = Container.objects.get(id=int(request.GET.get('id')))
        if request.POST:
            form = ContainerForm(request.POST)

            if form.is_valid():
                container.name = request.POST.get('name')
                container.weight = request.POST.get('weight')
                container.row = request.POST.get('row')
                container.type = Type.objects.get(id=int(request.POST.get('type')))
                container.place = Place.objects.get(id=int(request.POST.get('place')))
                container.owner = Owner.objects.get(id=int(request.POST.get('owner')))
                container.marchent = Marchent.objects.get(id=int(request.POST.get('marchent')))
                container.rent = request.POST.get('rent')
                container.contract_begin = request.POST.get('contract_begin')
                container.contract_end = request.POST.get('contract_end')
                container.description = request.POST.get('description')

                container.save()
            else:
                args['container'] = Container.objects.get(id=int(request.GET.get('id')))
                args['types'] = Type.objects.all().only('id', 'name')
                args['owners'] = Owner.objects.all().only('id', 'first_name', 'last_name', 'sur_name')
                args['marchents'] = Marchent.objects.all().only('id', 'first_name', 'last_name', 'sur_name')
                args['places'] = Place.objects.all().only('id', 'name')
                args['form'] = form

                return render_to_response('ajax/container.html', args)

            return HttpResponseRedirect('/dictionary/container?action=edit&id=' + str(container.id))
