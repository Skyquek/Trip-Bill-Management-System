from django.contrib.auth.models import User
from rest_framework import generics
from user.serializers import UserSerializer, ProfileSerializer, FriendshipSerializer
from user.models import Profile, Friendship
from rest_framework import permissions

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user_instance = serializer.save()
        Profile.objects.create(user=user_instance)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    