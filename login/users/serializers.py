from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ProfileSerializer, self).to_representation(instance)
        representation['photo'] = instance.photo.url
        return representation