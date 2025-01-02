from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from  theblog.models import Profile

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Save profile information here
        profile = Profile(user=user)
        profile.save()
        return response





class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    fields = [ 'bio', 'profile_image']
        
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
    
def add_profile(self, *args, **kwargs):
    unadded_users = User.objects.filter(profile__isnull=True)  # Corrected `is_null` to `isnull`
    for user in unadded_users:  # Changed `use` to `user`
        Profile.objects.create(user=user)  # Changed `username` to `user`

        










# Create your views here.
