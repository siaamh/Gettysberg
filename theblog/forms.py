from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Categories ,Comment 

# Fetching category choices dynamically
choices = Categories.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories','header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }
class AddCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        widgets=forms.Textarea(attrs={'class': 'form-control'}),


