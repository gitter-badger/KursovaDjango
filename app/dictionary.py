# coding: utf-8
import os
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.static import serve
from Kursova.settings import BASE_DIR
from core.models import Region, Distinct, City, Type, Place, Owner, Marchent, Container, Sex
import zipfile


def zip_dir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def clear_dir(path):
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e


@login_required(login_url='/login')
def get_list(request, model=None, template=None):
    list = model.objects.all()
    return render_to_response(template, locals(), context_instance=RequestContext(request))


@login_required(login_url='/login')
def get_form(request, model=None, model_form=None, name=None, back=None, now=None):
    args = {}
    args.update(csrf(request))
    args['request'] = request
    args['name'] = name
    args['back'] = back
    args['now'] = now

    if request.GET.get('action') == 'add':
        try:
            args['form'] = model_form()
            return render_to_response('form.html', args)
        except:
            return render_to_response('404.html')

    elif request.GET.get('action') == 'save':
        if request.POST:
            if request.GET.get('id'):
                args['model'] = model.objects.get(id=int(request.GET.get('id')))
                args['form'] = model_form(data=request.POST, instance=args['model'])
                messages.success(request, str(args['model']) + ' оновлено')
            else:
                args['form'] = model_form(request.POST)

            if args['form'].is_valid():
                args['form'].save()
            else:
                return render_to_response('form.html', args, context_instance=RequestContext(request))

        if request.GET.get('id'):
            return HttpResponseRedirect('/dictionary/' + now + '?action=edit&id=' + str(args['model'].id))
        else:
            return HttpResponseRedirect('/dictionary/' + back)

    elif request.GET.get('action') == 'edit':
        args['model'] = model.objects.get(id=int(request.GET.get('id')))
        args['form'] = model_form(instance=args['model'])
        return render_to_response('form.html', args, context_instance=RequestContext(request))

    elif request.GET.get('action') == 'remove':
        model.objects.get(id=int(request.GET.get('id'))).delete()
        return HttpResponseRedirect('/dictionary/' + back)


@login_required(login_url='/login')
def export(request, type=None):
    clear_dir(BASE_DIR + '/temp/')

    if type == 'xml':
        XMLSerializer = serializers.get_serializer("xml")
        xml_serializer = XMLSerializer()

        with open(os.path.join(BASE_DIR + '/temp', 'regions.xml'), 'w') as out:
            xml_serializer.serialize(Region.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'sex.xml'), 'w') as out:
            xml_serializer.serialize(Sex.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'distincts.xml'), 'w') as out:
            xml_serializer.serialize(Distinct.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'cities.xml'), 'w') as out:
            xml_serializer.serialize(City.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'types.xml'), 'w') as out:
            xml_serializer.serialize(Type.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'places.xml'), 'w') as out:
            xml_serializer.serialize(Place.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'owners.xml'), 'w') as out:
            xml_serializer.serialize(Owner.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'marchents.xml'), 'w') as out:
            xml_serializer.serialize(Marchent.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'containers.xml'), 'w') as out:
            xml_serializer.serialize(Container.objects.all(), stream=out)

        zp_name = 'dump_xml.zip'
        zp = zipfile.ZipFile(os.path.join(BASE_DIR + '/dump/', zp_name), "w")
        zip_dir(BASE_DIR + '/temp/', zp)
        zp.close()

        return serve(request, os.path.basename(os.path.join(BASE_DIR + '/dump', zp_name)),
                     os.path.dirname(os.path.join(BASE_DIR + '/dump', zp_name)))

    elif type == 'json':
        XMLSerializer = serializers.get_serializer("json")
        json_serializer = XMLSerializer()

        with open(os.path.join(BASE_DIR + '/temp', 'regions.json'), 'w') as out:
            json_serializer.serialize(Region.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'sex.json'), 'w') as out:
            json_serializer.serialize(Sex.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'distincts.json'), 'w') as out:
            json_serializer.serialize(Distinct.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'cities.json'), 'w') as out:
            json_serializer.serialize(City.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'types.json'), 'w') as out:
            json_serializer.serialize(Type.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'places.json'), 'w') as out:
            json_serializer.serialize(Place.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'owners.json'), 'w') as out:
            json_serializer.serialize(Owner.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'marchents.json'), 'w') as out:
            json_serializer.serialize(Marchent.objects.all(), stream=out)

        with open(os.path.join(BASE_DIR + '/temp', 'containers.json'), 'w') as out:
            json_serializer.serialize(Container.objects.all(), stream=out)

        zp_name = 'dump_json.zip'
        zp = zipfile.ZipFile(os.path.join(BASE_DIR + '/dump/', zp_name), "w")
        zip_dir(BASE_DIR + '/temp/', zp)
        zp.close()

        return serve(request, os.path.basename(os.path.join(BASE_DIR + '/dump', zp_name)),
                     os.path.dirname(os.path.join(BASE_DIR + '/dump', zp_name)))


def info(request, id=None, model=None):
    entity = model.objects.get(pk=id)
    containers = entity.container_set.all()
    return render_to_response('info.html', locals())