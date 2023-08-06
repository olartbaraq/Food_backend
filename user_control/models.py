from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, PermissionsMixin,  BaseUserManager
    )
# Create your models here.



class CustomUserManager(BaseUserManager):
    """_summary_

    Args:
        BaseUserManager (_type_): _description_

    Returns:
        _type_: _description_
    """

    def _create_user(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Returns:
            _type_: _description_
        """

        if not email:
            raise ValueError("email is required")
        
        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Returns:
            _type_: _description_
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('firstname', 'admin')
        extra_fields.setdefault('mobile', '08166893113')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser must have is_active=True')

        return self._create_user(email, password, **extra_fields)




class CustomUser(AbstractBaseUser, PermissionsMixin):
    """_summary_

    Args:
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    firstname = models.CharField(max_length=50, blank=False, null=False, error_messages= {
        "max_length": 'This field must not be more than 50 characters',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    lastname = models.CharField(max_length=50, blank=False, null=False, error_messages= {
        "max_length": 'This field must not be more than 50 characters',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False, error_messages= {
        "max_length": "This field must not be more than 254 characters",
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
        "unique": "This email address has already been used",
    })
    address = models.CharField(max_length=255, blank=False, null=False, default= "Ibadan", error_messages= {
        "max_length": 'This field must not be more than 100 characters',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    mobile = models.PositiveBigIntegerField(unique=True, null=False, blank=False, error_messages= {
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
        "unique": "This mobile number has already been used",
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = "Custom User"

