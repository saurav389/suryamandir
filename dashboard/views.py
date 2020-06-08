from django.shortcuts import render
from blog.models import BlogPost
# Create your views here.
def dashboard_view(request):
	

    return render(request,"dashboard.html",{})