from django.urls import path
from .views import PasswordGeneratorLevel1, PasswordGeneratorLevel2, PasswordGeneratorLevel3, UserRegistration, \
    PasswordAplication, Show_all_userpasswords, User_passwords
from .views import Login

urlpatterns = [
    path('password_lvl1/', PasswordGeneratorLevel1.as_view()),
    path('password_lvl2/', PasswordGeneratorLevel2.as_view()),
    path('password_lvl3/', PasswordGeneratorLevel3.as_view()),
    path('register/', UserRegistration.as_view()),
    path('password_aplication/', PasswordAplication.as_view()),
    path("login/", Login.as_view()),
    path("all/", Show_all_userpasswords.as_view()),
    path('user_info/',User_passwords.as_view()),
]
