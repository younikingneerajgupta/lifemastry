from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('registration/success/', views.registration_success, name='registration_success'),
     path("send_otp",views.send_otp,name="send otp"),    path('registration/result/', views.result, name='result'),  # 'result' page URL inside 'registration'
    path('header/', views.header_view, name='header_view'),
]
