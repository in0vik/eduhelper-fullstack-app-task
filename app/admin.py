from django.contrib import admin
from .models import SavedAnswer

# Register the model so we can manage SavedAnswer in the Django admin
admin.site.register(SavedAnswer)
