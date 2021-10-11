from django.urls import path
from django.utils.translation import templatize
from members.views import EditProfileView, UserRegisterView,ChangePasswordView,PasswordSuccessView
from django.contrib.auth import views as auth_views
# from blogapp import views


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',EditProfileView.as_view(),name='edit_profile'),
    path('password/',ChangePasswordView.as_view()),
    path('password_success',PasswordSuccessView,name='password_success')
]
