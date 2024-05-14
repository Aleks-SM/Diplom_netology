from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response

from .models import ConfirmEmailToken
from .serializers import UserSerializer

def index_page(request):
    return HttpResponse("Hello")

class RegisterAccount(APIView):
    """
    регистрация пользователей
    """
    def post(self, request, *args, **kwargs):
        """
        Create new user
        """
        # проверяем аргументы
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            # проверка пароля
            try:
                validate_password(request.data['password'])
            except Exception as password_errors:
                error_list = []
                for error in password_errors:
                    error_list.append(error)
                return JsonResponse({'Status': False, 'Errors': {'password': error_list}})
            else:
                # проверка имени пользователя
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})
        return JsonResponse({'Status': False, 'Errors': 'Указаны не все обязательные аргументы'})


class ConfirmAccount(APIView):
    """
    потверждение почты
    """
    def post(self, request, *args, **kwargs):
        """
        Confirm user email
        """
        # проверяем аргументы
        if {'email', 'token'}.issubset(request.data):
            token = ConfirmEmailToken.objects.filter(user__email=request.data['email'],
                                                     key=request.data['token']).first()
            if token:
                token.user.is_active = True
                token.user.save()
                token.delete()
                return JsonResponse({'Status': True})
            else:
                return JsonResponse({'Status': False, 'Errors': 'Неправильно указан токен или email'})
        return JsonResponse({'Status': False, 'Errors': 'Указаны не все обязательные аргументы'})


class AccountDetail(APIView):
    """

    """
    # получить данные
    def get(self, request: Request, *arg, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)

        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        # проверка обязательных аргументов
        if 'password' in request.data:
            errors = {}
            # проверка пароля
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                error_list = []
                for error in password_error:
                    error_list.append(error)
                return JsonResponse({'Status': False, 'Errors': {'password': error_list}})
            else:
                request.user.set_password(request.data['password'])

        user_serialiser = UserSerializer(request.user, data=request.data, partial=True)
        if user_serialiser.is_valid():
            user_serialiser.save()
            return JsonResponse({'Status': True})
        else:
            return JsonResponse({'Status': False, 'Errors': user_serialiser.errors})



class LoginAccount(APIView):
    """
    авторизация пользователя
    """
    def post(self, request, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'],
                                password=request.data['password'])
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)
                    return JsonResponse({'Status': True, 'Token': token.key})
            return JsonResponse({'Status': False, 'Errors': 'Авторизация не удалась'})
        return JsonResponse({'Status': False, 'Errors': 'Указаны не все обязательные аргументв'})

