from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    """
    Each Post will be a new table in the db 
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    # optional
    # pic = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # This is same as java toString method, the job is print friendly text to represent the object
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        """The function required to redirect to the post detail after create
            a new post

        Returns:
            str: The url
        """ 
        return reverse('post-detail', kwargs={'pk': self.pk})