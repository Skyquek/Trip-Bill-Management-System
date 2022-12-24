from django.http import HttpResponse

def index(request) -> HttpResponse:
    """A dummy docstring"""
    return HttpResponse("Hello, world. You're at the polls index")
