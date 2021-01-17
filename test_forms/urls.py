from django.urls import path
from . import views


urlpatterns = [
    path('', views.input_form, name='main_activity'),
    path('done/', views.done, name='done'),
]