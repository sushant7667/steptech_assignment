from rest_framework import serializers
from .models import *

class userserializer(serializers.ModelSerializer):
    # ... existing code ...
    class Meta:
        model = User
        fields = '__all__'