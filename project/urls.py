"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book.views import show_main_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('profile/', include('user_profile.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('autentifikasi/', include('autentifikasi.urls')),
    path('api/books/', include('book.urls')),
    path('book/<int:book_id>/', show_main_book, name='show_main_book'),
    path('forum/', include('forum.urls')),
]
