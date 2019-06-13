from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/newacc/login/")
def article_create(request):
    return render(request, "Blog/article_create.html")

# Create your views here.
