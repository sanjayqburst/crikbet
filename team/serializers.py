from django.db.models import fields
from .models import Teams
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model=Teams
        fields="__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance
