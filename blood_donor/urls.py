from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns =[
        path('registration/',views.registration, name='registration'),

        path('profile/',views.donorProfile,name='profile'),

        path('login/',views.donorLogin, name='login'),
        path('logout/',views.donorLogout,name='logout'),

        path('edit-information/',views.editInformation,name='edit-profile'),
        
        path('change-password/',auth_views.PasswordChangeView.as_view(template_name='blood_donor/change_password.html'),name='password_change'),
        path('change-password-done/',auth_views.PasswordChangeView.as_view(template_name='blood_donor/change_password_done.html'),name='password_change_done'),

        path('delete-account/',views.deleteAccount,name='delete_account'),

        path('set-status',views.setStatus,name='set-status')


        
]