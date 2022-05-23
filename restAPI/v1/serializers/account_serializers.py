from rest_framework import serializers
from account.models import User, UserType, CustomerID


class CustomerIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerID
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    customer_uuids = CustomerIDSerializer(many=True, read_only= True)
    class Meta:
        model = User
        fields = ('id', 'name', 'surname',
                  'phone', 'fin','location', 'id_card_photo', 'user_type', 'customer_uuids', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'], 
            surname=validated_data['surname'], 
            password=validated_data['password'],
            phone=validated_data['phone'], 
            fin=validated_data['fin'], 
            user_type=validated_data['user_type'], 
            location=validated_data['location']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'surname',
                  'phone', 'fin','location', 'id_card_photo', 'user_type', 'customer_uuids', 'password')

class UserTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserType
        fields = "__all__"

