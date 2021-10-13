from rest_framework import serializers
from .models import UserMatchPlayer




class UserMatchPlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for handling UserMatchPlayer View.
    """
    class Meta:
        model=UserMatchPlayer
        fields="__all__"

    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance