from django.urls import path
from . import views

app_name = 'flower'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
]
