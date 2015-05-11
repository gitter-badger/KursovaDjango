# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required(login_url='/login')
def get_list(request, model=None, template=None):
    list = model.objects.all()
    return render_to_response(template, locals())


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

        if args['model']:
            return HttpResponseRedirect('/dictionary/' + now + '?action=edit&id='+str(args['model'].id))
        else:
            return HttpResponseRedirect('/dictionary/' + back)

    elif request.GET.get('action') == 'edit':
        args['model'] = model.objects.get(id=int(request.GET.get('id')))
        args['form'] = model_form(instance=args['model'])
        return render_to_response('form.html', args, context_instance=RequestContext(request))

    elif request.GET.get('action') == 'remove':
        model.objects.get(id=int(request.GET.get('id'))).delete()
        return HttpResponseRedirect('/dictionary/' + back)