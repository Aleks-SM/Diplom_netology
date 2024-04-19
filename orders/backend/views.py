from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView

from .serializers import UserSerializer

def index_page(request):
    return HttpResponse("Hello")

class RegisterAccount(APIView):
    """

    """
    def post(self, request, *args, **kwargs):
        """
        проверяем аргументы
        """
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
        return JsonResponse({'Status': False, 'Errors': 'Не указаны обязательные значения'})
