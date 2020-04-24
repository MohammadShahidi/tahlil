from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # username --> nationalID
    # password --> sample pass
    # email
    # first_name
    # last_name

    def __str__(self):
        return self.user.first_name + self.user.last_name
