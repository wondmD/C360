from django.contrib.auth.backends import BaseBackend
from .models import myusers

class myusersBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = myusers.objects.get(username=username)
        except myusers.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
