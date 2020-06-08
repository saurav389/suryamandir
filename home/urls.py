from django.urls import path
from django.conf.urls.static import static
from .views import home_view,Post_view,team_view,contact_view,donation_view,success_view,search_view


urlpatterns = [
    path('',home_view,name= 'home'),
    path('search/',search_view,name='search'),
    path('donation/',donation_view,name='donation'),
    path('charge/',success_view,name='charge'),
    path('post/',Post_view,name='post'),
    path('team/',team_view,name='team'),
    path('contact/',contact_view,name='contact')

]