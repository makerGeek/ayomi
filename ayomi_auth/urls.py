from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^login/',  auth_views.login,{'template_name':'ayomi_auth/login.html'}, name='login'),
    url(r'^logout/',  auth_views.logout, {'next_page':reverse_lazy('login')}, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^profile/', login_required(ProfileView.as_view()), name='profile'),
    url(r'^update_email/', login_required(UpdateEmail.as_view()), name='update_email'),
]
