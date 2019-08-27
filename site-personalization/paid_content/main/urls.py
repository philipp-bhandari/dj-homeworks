from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.urls import path

from articles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.show_articles, name='articles'),
    path('articles/<int:id>/', views.show_article, name='article'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('', RedirectView.as_view(url='articles/')),
]
