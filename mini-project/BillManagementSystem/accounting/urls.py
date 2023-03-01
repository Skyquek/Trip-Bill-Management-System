from django.urls import path

from . import views
from strawberry.django.views import AsyncGraphQLView
from .schema import schema

urlpatterns = [
    path('', views.index, name='index'),
    path('graphql', AsyncGraphQLView.as_view(schema=schema)),
]