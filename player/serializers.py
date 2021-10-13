from django.db.models import fields
from rest_framework import serializers
from .models import Players

class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for handling Player API request and storing the fields.
    """
    class Meta:
        model=Players
        fields="__all__"
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance