from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Categories ,Profile , Comment , city , Follower
from .forms import PostForm, EditForm ,AddCommentForm 
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        cat_menu = Categories.objects.all()
        context["cat_menu"] = cat_menu

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

def CategoryView(request, cats):
    category_posts = Post.objects.filter(categories=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Categories.objects.all()
    return render(request, 'categories-list.html', {'cat_menu_list': cat_menu_list})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-details', kwargs={'pk': self.object.pk})

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def WriterPostsView(request, writer_id):
    writer_posts = Post.objects.filter(author_id=writer_id)
    return render(request, 'writer-posts', {'writer_posts': writer_posts})


from django.shortcuts import render
from django.contrib.auth.models import User

def WriterListsView(request):
    writer_list = Profile.objects.all()
    return render(request, 'writer-list.html', {'writer_list': writer_list})


from django.http import JsonResponse


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'addcomment.html'
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])  # Link the comment to the post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('article-details', kwargs={'pk': self.object.post.pk})  # Redirect to the post's detail view




def following(request, pk):
    follow = False
    profile = get_object_or_404(Profile, pk=pk)

    if not follow:
        Follower.objects.create(user=profile, follower=request.user.profile)
        follow = True
    else:
        Follower.objects.filter(user=profile, follower=request.user.profile).delete()
        follow = False

    return HttpResponseRedirect(reverse('writer-post', args=[str(pk)]))










     
        




def get_weather(request):
    cities = city.objects.all()  # Correct method to retrieve all city objects
    weather_data = []

    for City in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={City.name}&appid=31abce807a1d732972eb231f2fdbcbdb"
        response = requests.get(url)
        weather_data.append(response.json())
        
    return render(request, 'weather.html', {'weather_data': weather_data})
import requests
from django.shortcuts import render

import requests
from django.shortcuts import render

def search_weather(request):
    weather_data = {}
    error_message = None

    if 'city' in request.POST:
        City = request.POST['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid=31abce807a1d732972eb231f2fdbcbdb"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            weather_data['main']['temp'] = weather_data['main']['temp'] - 273.15
        else:
            error_message = "Failed to retrieve data. Please check the city name or try again later."
    
    context = {
        'weather_data': weather_data,
        'error_message': error_message
    }
    return render(request, 'weatherq.html', context)



def get_result(request):
    url = "https://api.soccersapi.com/v2.2/leagues/?user=siamhussain394&token=faed1db5f2dafe9a39c5d5cb81a733e8&t=list"
    response = requests.get(url)
    data = response.json()  # Parse the JSON response

    return render(request, 'result.html', {'data': data})
