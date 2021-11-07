from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import UserMessage


def login(request):
    m = UserMessage.objects.all()
    count_bro = m.filter(message='Bro!').count()
    count_sis = m.filter(message='Sis!').count()
    context = {'count_bro': count_bro, 'count_sis': count_sis}
    return render(request, 'main/login.html', context)


@login_required
def logged_in(request):
    try:
        m = UserMessage.objects.order_by('date_time')
        last = m.last()
        last_user = last.user.first_name
        last_date = last.date_time.strftime("%H:%M")
        last_message = last.message
        data = {'last_user': last_user, 'last_date': last_date, 'last_message': last_message}
        return render(request, 'main/main.html', data)
    except AttributeError:
        return render(request, 'main/main.html')


def message_send(request):
    user = request.user
    if 'bro' in request.POST:
        new_message = 'Bro!'
    elif 'sis' in request.POST:
        new_message = 'Sis!'
    m = UserMessage.objects.create(user=user, message=new_message)
    context = {'data': m, 'user': user}
    return redirect('/logged_in', context)
