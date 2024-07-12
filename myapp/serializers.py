# Manually Created.....

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

"""
Serializers in DRF are used to convert complex data types (like queryset instances or model instances) 
into native Python datatypes that can then be easily rendered into JSON, XML, or other content types. 
They also handle deserialization, allowing parsed data to be converted back into complex types.

"""
