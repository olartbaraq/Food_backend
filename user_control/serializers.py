from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):

    """_summary_

    Args:
        serializers (_type_): _description_
    """ 

    email = serializers.EmailField()
    lastname = serializers.CharField()
    firstname = serializers.CharField()
    address = serializers.CharField()
    mobile = serializers.IntegerField()
    password = serializers.CharField(min_length = 10, write_only=True)
    
    class Meta:
        model = CustomUser
        #fields=[ 'email', 'password', 'mobile', 'lastname', 'firstname', 'address']
        exclude = ("groups", "user_permissions")
    
    def validate(self, attrs):
        """
        validation to check if emails already exists in the database
        """
        
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()
        mobile_exists = CustomUser.objects.filter(mobile=attrs['mobile']).exists()
        
        if email_exists: 
            raise ValidationError('Email already exists')
        if mobile_exists: 
            raise ValidationError('Mobile Number already exists')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data) 
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):

    """_summary_

    Args:
        serializers (_type_): _description_
    """

    email = serializers.EmailField()
    password = serializers.CharField()
    
    
class UpdatePasswordSerializer(serializers.Serializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    
    email = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields= ['email', 'password']
    
    
class DeleteUserSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ("email", )