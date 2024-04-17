from rest_framework.serializers import ModelSerializer
from orders.backend.models import User, Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'apartment',
                  'user', 'phone')
        fields = ('id',)

class UserSerializer(ModelSerializer):
    class Mets:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company'
                  'position', 'conracts')
        fields = ('id',)
