from django.urls import path, include

urlpatterns = [
    path('accounts/signup/', include('allauth.urls'))
]
