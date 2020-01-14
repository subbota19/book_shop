from django.shortcuts import render, redirect
from django.core.cache import cache
from django.conf import settings
from django.views import View
from .forms import SubscribersForm
from .models import Subscribers
import datetime, memcache


# Create your views here.

class ViewSubscribersForm(View):

    def get(self, request):

        return render(request, 'register_form/sign_in.html', {'form': SubscribersForm(), 'error': ''})

    def post(self, request):
        form = SubscribersForm(request.POST)
        form.is_valid()
        is_user = Subscribers.objects.all().filter(user_name=form.cleaned_data['user_name'],
                                                   password=form.cleaned_data['password'])
        if is_user:
            cache.set(is_user[0].user_name, datetime.datetime.now(), settings.USER_LAST_SEEN_TIMEOUT)
            is_user[0].is_online = True
            request.session['user'] = is_user[0].user_name
            return redirect('books_image')
        else:
            return render(request, 'register_form/sign_in.html',
                          {'form': SubscribersForm(),
                           'error': 'We cannot find an account with this username or password '})


def sign_up(request):
    form = SubscribersForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        check_user_name = Subscribers.objects.filter(user_name=data['user_name'])
        check_email = Subscribers.objects.filter(email=data['email'])
        if check_user_name or check_email:
            return render(request, 'register_form/sign_up.html',
                          {'form': SubscribersForm(), 'error': 'This user is already taken'})
        else:
            user = Subscribers.objects.create(user_name=data['user_name'], password=data['password'],
                                              email=data['email'], is_online=True)
            user.save()
            cache.set(user.user_name, datetime.datetime.now(), settings.USER_LAST_SEEN_TIMEOUT)
            # request.session['user'] = user.user_name
            return redirect('books_image')
    else:
        return render(request, 'register_form/sign_up.html', {'form': SubscribersForm()})


def redirect_register(request):
    return redirect('sign_in', permanent=True)
