from rest_framework import serializers
from .models import UserMatches




class UserMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserMatches
        fields="__all__"

    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance