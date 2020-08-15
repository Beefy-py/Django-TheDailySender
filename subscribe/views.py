from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import Subscribe


# Create your views here.
def home(request):
    context = {'text': 'Thanks for Subbing'}
    return render(request, 'subscribe/home.html', context)


def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscription = Subscribe(
                name=subscribe_form.cleaned_data['name'].capitalize(),
                email=subscribe_form.cleaned_data['email'],
                country=subscribe_form.cleaned_data['country']
            )

            subscription.save()
            return redirect('home')

    else:
        subscribe_form = SubscribeForm()
    context = {'form': subscribe_form}
    return render(request, 'subscribe/subscribe.html', context=context)


def unsubscribe(request):
    if request.method == 'POST':
        unsubscribe_form = UnsubscribeForm(request.POST)
        if unsubscribe_form.is_valid():
            e = Subscribe.objects.filter(email=unsubscribe_form.cleaned_data['email'])
            e.delete()
            return redirect('home')

    else:
        unsubscribe_form = UnsubscribeForm()
    context = {'form': unsubscribe_form}
    return render(request, 'subscribe/unsubscribe.html', context)


def subscribers(request):
    context = {
        'all_subbers': Subscribe.objects.all()
    }
    return render(request, 'subscribe/view_subscribers.html', context)