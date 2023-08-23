from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """This is the user profile class

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_figs')

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f'{self.user.username} Profile'
    
    def save(self):
        """
        Rewrite save methon to resize image use PIL
        """
        # Run the super class to save the profile image 
        super().save()
        img = Image.open(self.image.path)

        # resize and save the profile image
        if img.height >300 or img.width >300:
            size = (300,300)
            img.thumbnail(size)
            img.save(self.image.path)