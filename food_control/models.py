from django.db import models


class FoodCategory(models.Model):
    """Food category model

    Args:
        models (_type_): _description_
    """
    
    name = models.CharField(max_length=50, blank=False, null= False, error_messages= {
        "max_length": 'This field must not be more than 50 characters',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    starting_price = models.FloatField(blank=False, null= False, error_messages= {
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    restaurant_which_belongs = models.ForeignKey('restaurant_control.Restaurant', on_delete=models.CASCADE, related_name='restaurant_which_belongs') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.name} {self.starting_price}"
    
    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = "Food Category"




class Food(models.Model):
    """Food model 

    Args:
        models (_type_): _description_
    """
    
    name = models.CharField(max_length=50, blank=False, null= False, error_messages= {
        "max_length": 'This field must not be more than 50 characters',
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    price = models.FloatField(blank=False, null= False, error_messages= {
        "null": "This field must not be empty",
        "blank": "This field must not be empty",
    })
    restaurant_belongs_to = models.ForeignKey('restaurant_control.Restaurant', on_delete=models.CASCADE, related_name='restaurant_belongs_to') 
    category_belongs_to = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_category_belongs')
    time_to_make = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {self.price}"
    
    class Meta:
        ordering = ('-created_at', )
        verbose_name_plural = "Food"
