"""buildstudydesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

from .views import index, new_visit, edit_visit, remove_visit, edit_study, edit_sampletp, remove_sampletp, new_sampletp, new_group, edit_group, remove_group

urlpatterns = [
    path('',views.index, name='index'),     
    path('new_visit', new_visit, name="main_app_new_visit"),
	path('new_sampletp', new_sampletp, name="main_app_new_sampletp"),
	path('new_group', new_group, name="main_app_new_group"),
    path('<int:pk>/edit_sampletp', edit_sampletp, name="edit_sampletp"),
    path('<int:pk>/edit_group', edit_group, name="edit_group"),
    path('<int:pk>/remove-sampletp', remove_sampletp, name="remove_sampletp"),
    path('<int:pk>/remove-group', remove_group, name="remove_group"),
    path('<int:pk>/edit-visit', edit_visit, name="edit_visit"),
    path('<int:pk>/remove-visit', remove_visit, name="remove_visit"),
    path('<int:pk>/edit-study', edit_study, name="edit_study")
]
