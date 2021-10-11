from django.views.generic.edit import UpdateView
from members.forms import SignupForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from members.forms import SignupForm,EditProfileForm,PasswordChangingForm
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

class UserRegisterView(CreateView):
    form_class=SignupForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class EditProfileView(UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('index')

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class= PasswordChangingForm
    template_name='registration/change_password.html'
    success_url=reverse_lazy('password_success')

def PasswordSuccessView(request):
    return render(request,'registration/password_success.html',{})