from django.urls import path, include
from user import views

urlpatterns = [
    path('users/', views.UserCreate.as_view()),
    path('profile/', views.ProfileDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]