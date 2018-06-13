from django.contrib.auth import login, authenticate, get_user_model
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse
from django.views.generic import FormView, DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

from .forms import UserForm


class RegisterView(FormView):
    template_name = 'ayomi_auth/register.html'
    form_class = UserForm
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.clean_password2(),
                                        first_name =form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
        user = authenticate(username=user.username, password=form.clean_password2())
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'ayomi_auth/profile.html'
    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.pk)


class UpdateEmail(UpdateView):
    model = get_user_model()
    fields = ['email']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.pk)
    def post(self, request, *args, **kwargs):
        super(UpdateEmail, self).post(request, *args, **kwargs)
        return JsonResponse({"email":self.object.email})
