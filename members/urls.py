from django.urls import path
from .views import RegisterView,EditProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/edit-profile/',EditProfileView.as_view(),name='edit-profile')
]
