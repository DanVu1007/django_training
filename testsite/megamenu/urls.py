from django.urls import path
from . import views

app_name = 'megamenu'

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
]
