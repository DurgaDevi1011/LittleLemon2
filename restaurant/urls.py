from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView


urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.singleMenuView.as_view()),
    path('',TemplateView.as_view(template_name='index.html'), name='indexpage'),
    path('api-token-auth/', obtain_auth_token),
]