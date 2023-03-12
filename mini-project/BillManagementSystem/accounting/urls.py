from django.urls import path

from . import views
from strawberry.django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('', views.index, name='index'),
    path('graphql', GraphQLView.as_view(schema=schema)),
]