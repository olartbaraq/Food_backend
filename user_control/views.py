from datetime import datetime
from .serializers import (
    CreateUserSerializer, CustomUser, LoginUserSerializer, UpdatePasswordSerializer, DeleteUserSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from food_backend.utils import create_jwt_pair_for_user
from .permissions import ReadOnly, AuthorOrReadOnly


# Create your views here.

class  CreateUserView(ModelViewSet):

    """_summary_

    Args:
        ModelViewSet (_type_): _description_
    """
    http_method_names = ['post']
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AuthorOrReadOnly, )

    def create(self, request: Request):
        """summary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        
        data = request.data
        valid_request = self.serializer_class(data=data)
        if valid_request.is_valid():
            valid_request.save()
            response = {
                "message": "User created successfully",
                "data": valid_request.data
            }

            return Response(
                data=response, status = status.HTTP_201_CREATED
            )

        return Response(data=valid_request.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(ModelViewSet):
    http_method_names = ['post']
    queryset = CustomUser.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = (AuthorOrReadOnly, )
    
    
    def create(self, request: Request):

        """_summary_

        Args:
            request (_type_): _description_
        """
        
        data = request.data
        valid_request = self.serializer_class(data=data)
        valid_request.is_valid(raise_exception=True)

        email = valid_request.validated_data.get("email")
        password = valid_request.validated_data.get("password")
        
       
        user = authenticate(email=email, password=password)
        
        if user is not None:
            
            tokens = create_jwt_pair_for_user(user)
            
            response = {
                "message": "User Logged in successfully",
                "data": {
                    "email": user.email,
                    "address": user.address,
                    "mobile": user.mobile,
                    "lastname": user.lastname,
                    "firstname": user.firstname,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                    "last_login": user.last_login,
                    },
                "Authorization": tokens
            }
            
            return Response(
                data=response, status=status.HTTP_200_OK
            )
            
        return Response(
            {"error": "Invalid username or password"}
        )
            
class UpdatePasswordView(ModelViewSet):
    serializer_class = UpdatePasswordSerializer
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()
    permission_classes = (AuthorOrReadOnly, )
    
    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)
        
        user = CustomUser.objects.filter(email = valid_request.validated_data["email"])
        
        if not user:
            return Response(
            {"error": "User not found"},
            status=status.HTTP_400_BAD_REQUEST
            )
        
        user = user[0]
        user.set_password(valid_request.validated_data["password"])
        user.save()
         
        return Response(
            {"message": "User password changed successfully"},
            status=status.HTTP_200_OK
        )
        

class DeleteUserView(ModelViewSet):
    """_summary_

    Args:
        ModelViewSet (_type_): _description_
    """
    serializer_class = DeleteUserSerializer
    http_method_names = ['post']
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,  AuthorOrReadOnly)
    
    def create(self, request: Request):
        """method to delete a user

        Args:
            request (Request): _description_
        """
        
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)
        
        user = CustomUser.objects.filter(email = valid_request.validated_data["email"])
        
        if not user:
            #raise Exception("User not found")
        
            return Response(
            {"error": "User not found"},
            status=status.HTTP_400_BAD_REQUEST
            )
        
        user = user[0]
        user.delete()
         
        return Response(
            {"message": "User account deleted successfully"},
            status=status.HTTP_200_OK
        )