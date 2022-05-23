from django.contrib.auth import user_logged_in
from rest_framework import status, generics

from rest_framework.response import Response

from account.models import (
    User,
    UserType, 
    CustomerID
)

from restAPI.utils.account_utils import jwt as custom_jwt

from rest_framework_simplejwt.views import TokenObtainPairView

from restAPI.v1.serializers.account_serializers import CustomerIDSerializer, RegisterSerializer, UserSerializer, UserTypeSerializer

from rest_framework.views import APIView

import traceback


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUser(APIView):
    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except:
            return Response({"detail": "Login olmamısınız"}, status=status.HTTP_400_BAD_REQUEST)
        


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = custom_jwt.jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(id=acces_token.get("user_id")).last()
        user_logged_in.send(sender=type(user), request=request, user=user)

        user_details = UserSerializer(user)

        data["user_details"] = user_details.data
        return Response(data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class UserTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class UserTypeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class CustomerIDListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerID.objects.all()
    serializer_class = CustomerIDSerializer

class CustomerIDDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerID.objects.all()
    serializer_class = CustomerIDSerializer