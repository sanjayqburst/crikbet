from django.db.models import fields
from rest_framework import serializers
from .models import Matches

class MatchSerializer(serializers.ModelSerializer):
    """
    Serializer for handling matchview.
    """

    class Meta:
        model=Matches
        fields="__all__"

    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance
