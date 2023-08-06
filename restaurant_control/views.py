from .serializers import (
    CreateRestaurantSerializer, Restaurant, UpdateRestaurantSerializer, DeleteRestaurantSerializer,
    ListRestaurantSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
# Create your views here.


class CreateRestaurantView(ModelViewSet):
    """create the api view for creating a new restaurant

    Args:
        ModelViewSet (_type_): _description_
    """
    
    http_method_names = ['post']
    queryset = Restaurant.objects.all()
    serializer_class = CreateRestaurantSerializer
    permission_classes = (IsAdminUser, )
    
    
    def create(self, request: Request): 
        """create a new restaurant method

        Args:
            request (Request): _description_
        """
        
        data = request.data
        valid_request = self.serializer_class(data=data)
        if valid_request.is_valid():
            valid_request.save()
            response = {
                "message": "Restaurant created successfully",
                "data": valid_request.data
            }

            return Response(
                data=response, status = status.HTTP_201_CREATED
            )

        return Response(data=valid_request.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    
class UpdateRestaurantView(ModelViewSet):
    """Api View for updating a restaurant

    Args:
        ModelViewSet (_type_): _description_
    """
    http_method_names = ['post']
    queryset = Restaurant.objects.all()
    serializer_class = UpdateRestaurantSerializer
    permission_classes = (IsAdminUser, )
    
    
    def create(self, request: Request):
        """post method for updating a restaurant

        Args:
            request (Request): _description_
        """
        
        data = request.data
        valid_request = self.serializer_class(data=data)
        valid_request.is_valid(raise_exception=True)
        
        new_restaurant_name = valid_request.validated_data['new_restaurant_name']
        address = valid_request.validated_data['address']
        description = valid_request.validated_data['description']
        
        
        restaurant = Restaurant.objects.filter(name = valid_request.validated_data['name'])
       
        if not restaurant:
            raise Exception("Restaurant not found")
        
        restaurant = restaurant[0]
        restaurant.name = new_restaurant_name
        restaurant.address = address
        restaurant.description = description
        restaurant.save()
         
        return Response(
            {"message": "Restaurant updated successfully"},
            status=status.HTTP_200_OK
        )
        
        
class DeleteRestaurantView(ModelViewSet):
    """API view for deleting a restaurant

    Args:
        ModelViewSet (_type_): _description_
    """
    
    http_method_names = ['post']
    queryset = Restaurant.objects.all()
    serializer_class = DeleteRestaurantSerializer
    permission_classes = (IsAdminUser, )
    
    def create(self, request: Request):
        """post a request to delete a restaurant

        Args:
            request (Request): _description_
        """
        
        data = request.data
        valid_request = self.serializer_class(data=data)
        valid_request.is_valid(raise_exception=True)

        restaurant = Restaurant.objects.filter(name = valid_request.validated_data['name'])
       
        if not restaurant:
            raise Exception("Restaurant not found")
        
        restaurant = restaurant[0]
        restaurant.delete()
        
        return Response(
            {"message": "Restaurant deleted successfully"},
            status=status.HTTP_200_OK
        )
        
        
class GetAllRestaurantView(ModelViewSet):
    """APi view to list all restaurant

    Args:
        ModelViewSet (_type_): _description_
    """
    
    http_method_names = ['get']
    queryset = Restaurant.objects.all()
    serializer_class = ListRestaurantSerializer
    permission_classes = (IsAdminUser, )
    
    def list(self, request: Request):
        """get request http method to list all restaurants

        Args:
            request (Request): _description_
        """
    
        response = super().list(request)
        data = {
            "message": "List all restaurant",
            "data": response.data
        }
        return Response(
            data=data, status = status.HTTP_200_OK
        )