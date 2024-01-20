from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Profile, Friendship

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_id', 'user', 'phone_number', 'currency', 'language', 'profile_picture']

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['friendship_id', 'user1', 'user2']
        
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']