from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

from .forms import ProfileRegisterForm
from .models import Article

from django.views.defaults import permission_denied


def show_articles(request):
    is_logged = request.user.is_authenticated
    has_subscription = False

    if is_logged:
        has_subscription = request.user.has_subscription

    articles = Article.objects.values('pk', 'title')

    if not has_subscription:
        articles = articles.filter(by_subscription=False)

    context = {
        'articles': articles,
        'is_logged': is_logged,
        'has_subscription': has_subscription
    }

    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    article = Article.objects.get(pk=id)

    context = {
        'article': article
    }

    return render(
        request,
        'article.html',
        context
    )


def subscribe(request):
    if request.method == 'POST':
        user = request.user

        user.has_subscription = True
        user.save()

        return redirect(reverse('articles'))

    return HttpResponseForbidden('<h1>403: METHOD NOT ALLOWED</h1>', content_type='text/html')


def signup(request):
    if request.method == 'POST':
        register_form = ProfileRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('login'))
    else:
        register_form = ProfileRegisterForm()

    context = {'form': register_form}

    return render(request, 'registration/signup.html', context)
