from rest_framework import serializers
from .models import MatchPlayer




class MatchPlayerSerializer(serializers.ModelSerializer):
    """
    Serialiszer for handling Match player data
    """
    class Meta:
        model=MatchPlayer
        fields="__all__"

    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        if instance is not None:
            instance.save()
            return instance