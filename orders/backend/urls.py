from django.urls import path
from .views import RegisterAccount, ConfirmAccount, LoginAccount

app_name = 'backend'
urlpatterns = [
    path("user/register", RegisterAccount.as_view(), name='register_user'),
    path("user/register/confirm", ConfirmAccount.as_view(), name='confirm_user'),
    path("user/login", LoginAccount.as_view(), name='login_user')
     ]