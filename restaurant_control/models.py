from django.db import models

# Create your models here.


class Restaurant(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=50, unique=True, blank=False, null=False, error_messages=
    {
        "max_length": 'This field must not be more than 50 characters',
        "unique": 'This restaurant name has already been registered',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    address = models.CharField(max_length= 254)
    description = models.TextField(default='we are the best at what we do', null=False, blank=False, error_messages=
    {
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Restaurant'
