"""
URL configuration for studymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth import logout
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_view, name='main_view'),
    path('add/',views.add_study, name='add_study'),
    path('edit/<int:pk>', views.edit_study, name='edit_study'),
    path('view/<int:pk>', views.view_study, name='view_study'),
    path('delete/<int:pk>', views.delete_study, name='delete_study'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='studies/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='studies/logged_out.html'), name='logout'),
]

