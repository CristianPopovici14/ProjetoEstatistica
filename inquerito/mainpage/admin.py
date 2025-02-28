from django.contrib import admin
from .models import Data  # Correct model import

admin.site.register(Data)  # Register the UserResponse model in admin
