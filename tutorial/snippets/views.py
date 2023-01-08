from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    query_set = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    query_set = Snippet.objects.all()
    serializer_class = SnippetSerializer
    