from django.urls import path
from users.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile

from django.contrib.auth import views as authViews 



urlpatterns = [
   	path('sign-up/', Signup, name='sign-up'),
   	path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('profile/<int:pk>', UserProfile, name='user-profile' ),
    path('profile/edit', EditProfile, name='edit-profile'),
   	path('changepassword/', PasswordChange, name='change_password'),
   	path('changepassword/done', PasswordChangeDone, name='change_password_done'),
   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	
] 