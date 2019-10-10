from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id', 'name', 'gender', 'description', 'book', 'picture',  'created'
        )