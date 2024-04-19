from rest_framework.serializers import ModelSerializer
from .models import User, Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'apartment',
                  'user', 'phone')
        read_only_fields = ('id',)
        extra_kwargs = {'write_only': True}

class UserSerializer(ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company',
                  'position', 'contacts', 'username')
        read_only_fields = ('id',)
