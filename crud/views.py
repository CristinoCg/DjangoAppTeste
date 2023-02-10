from django.shortcuts import render
from .models import Post
# Create your views here.
def list_view(request):
    return render(request, 'crud/home.html',{'posts':Post.objects.all()})
