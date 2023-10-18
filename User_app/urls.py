from django.urls import path
from .views import PasswordGeneratorLevel1, PasswordGeneratorLevel2, PasswordGeneratorLevel3, UserRegistration, \
    PasswordAplication
from .views import Login

urlpatterns = [
    path('password_lvl1/', PasswordGeneratorLevel1.as_view()),
    path('password_lvl2/', PasswordGeneratorLevel2.as_view()),
    path('password_lvl3/', PasswordGeneratorLevel3.as_view()),
    path('register/', UserRegistration.as_view()),
    path('password_aplication/', PasswordAplication.as_view()),
    path("login/", Login.as_view()),

]
