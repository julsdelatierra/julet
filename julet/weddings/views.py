import hashlib
from django.shortcuts import render_to_response as render, redirect, get_object_or_404 as get_or_404
from django.template.context import RequestContext as rc
from django.http import HttpResponse
from julet.weddings import wedding_code
from julet.weddings.models import *
from julet.weddings.forms import *
from django.utils.translation import ugettext_lazy as _
from BeautifulSoup import BeautifulSoup

def new(request):
    if not request.GET.__contains__('id'):
        return HttpResponse('404')
    if Wedding.objects.filter(id=request.GET['id']).count()==0:
        wedding = Wedding.objects.create(id=request.GET['id'])
    else:
        args = {
            'message':_(u'Lo sentimos, pero el sitio ya existe.')
        }
        return render('message.html', args, context_instance=rc(request))
    return redirect('/%s/panel/set_password/' % (wedding.id))

def view(request, id):
    wedding_id = None
    try:
        wedding = Wedding.objects.get(id=id)
        try:
            embed = BeautifulSoup(wedding.place_map)
            map_url = embed.iframe['src']
        except:
            map_url = ''
        wedding_id = wedding.id
        gifts = Gift.objects.filter(wedding=wedding_id)
        args = {'wedding':wedding, 'map_url':map_url, 'gifts':gifts}
        return render('view.html', args, context_instance=rc(request))
    except:
        wedding_id = id
    args = {'id':wedding_id}
    return render('new.html', args, context_instance=rc(request))

def panel(request, id):
    if not request.META.__contains__('HTTP_REFERER'):
        return redirect('/%s/panel/get_password/' % (id))
    wedding = get_or_404(Wedding, pk=id)
    info_form = InfoForm(instance=wedding)
    if request.POST:
        info_form = InfoForm(request.POST, instance=wedding)
        if info_form.is_valid():
            info_form.save()
            return redirect('/%s/panel/#info' % (wedding.id))
    gifts = Gift.objects.filter(wedding=wedding.id)
    args = {
        'gifts':gifts,
        'info_form':info_form,
        'wedding':wedding,
    }
    return render('panel.html', args, context_instance=rc(request))

def welcome(request, id):
    if not request.META.__contains__('HTTP_REFERER'):
        return redirect('/%s/panel/get_password/' % (id))
    wedding = get_or_404(Wedding, pk=id)
    if request.POST:
        wedding.welcome = request.POST['welcome']
        wedding.save()
    return redirect('/%s/panel/#welcome' % (wedding.id))

def gift(request, id):
    if not request.META.__contains__('HTTP_REFERER'):
        return redirect('/%s/panel/get_password/' % (id))
    if request.POST:
        wedding = get_or_404(Wedding, pk=id)
        Gift.objects.create(wedding=wedding.id, name=request.POST['name'])
    return redirect('/%s/panel/#gifts' % (wedding.id))

def delete(request, wedding, gift):
    if not request.META.__contains__('HTTP_REFERER'):
        return redirect('/%s/panel/get_password/' % (id))
    Gift.objects.get(pk=gift).delete()
    return redirect('/%s/panel/#gifts' % (wedding))

def mark_gift(request):
    gift = get_or_404(Gift,pk=request.GET['id'])
    gift.taken=True
    gift.save()
    return HttpResponse('1');

def get_password(request, id):
    wedding = get_or_404(Wedding,pk=id)
    message = None
    if request.POST:
        password1 = hashlib.sha224(request.POST['password']).hexdigest()
        password2 = wedding.password
        if password1 == password2:
            return redirect('/%s/panel/' % (id))
        else:
            message = _(u'Lo sentimos, password incorrecto, intenta de nuevo.')
    args = {'message':message}
    return render('get_password.html', args, context_instance=rc(request))

def set_password(request, id):
    wedding = get_or_404(Wedding,pk=id,password='')
    if request.POST:
        wedding.password = hashlib.sha224(request.POST['password']).hexdigest()
        wedding.save()
        return redirect('/%s/panel/' % (wedding.id))
    args = {}
    return render('set_password.html', args, context_instance=rc(request))
