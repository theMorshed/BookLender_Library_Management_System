from django.urls import path
from account.views import user_login, user_logout, register

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
