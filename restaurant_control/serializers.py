from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Restaurant



class CreateRestaurantSerializer(serializers.ModelSerializer):
    """serialzer to create a new restaurant

    Args:
        serializers (_type_): _description_
    """
    
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length= 254)
    description = serializers.CharField()
    
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'description')
        
        
    def validate(self, attrs):
        """
        validation to check if restaurant already exists in the database
        """
        
        name_exists = Restaurant.objects.filter(name=attrs['name']).exists()
        
        if name_exists: 
            raise ValidationError('Restaurant already exists')
        
        return super().validate(attrs)
    
    
    
class UpdateRestaurantSerializer(serializers.ModelSerializer):
    """serializer for updating a Restaurant

    Args:
        serializers (_type_): _description_
    """
    
    name = serializers.CharField(max_length=50)
    new_restaurant_name = serializers.CharField(max_length=50)
    address = serializers.CharField()
    description = serializers.CharField()
    
    class Meta:
        model = Restaurant
        fields = ('name', 'new_restaurant_name', 'description', 'address', )
        
        

class DeleteRestaurantSerializer(serializers.ModelSerializer):
    """class to delete a restaurant

    Args:
        serializers (_type_): _description_
    """

    name = serializers.CharField()
    
    class Meta:
        model = Restaurant
        fields = ('name', )
        
        
class ListRestaurantSerializer(serializers.ModelSerializer):
    """class to list all restaurant in the database

    Args:
        serializers (_type_): _description_
    """
    
    class Meta:
        model = Restaurant
        exclude = ()