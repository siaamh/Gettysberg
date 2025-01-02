from django.urls import path
from django.contrib import admin
from .views import HomeView, ArticleDetailView, AddPostView,get_result,get_weather,DeletePost,EditPost, AddCommentView,CategoryListView ,CategoryView ,WriterPostsView , LikeView , WriterListsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-details"),
    path('admin/', admin.site.urls, name="admin"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/<int:pk>/delete_post/', DeletePost.as_view(), name="delete-post"),
    path('article/<int:pk>/edit_post/', EditPost.as_view(), name="edit-post"),
    path('category/<str:cats>/', CategoryView, name="categories"),
    path('categories-list',CategoryListView,name="categories-list"),
    path('like-post/<int:pk>',LikeView,name="like-post"),
    path('writer/<int:writer_id>/', WriterPostsView, name='writer-posts'),
    path('writer-list/',WriterListsView,name="writer-list"),
    path('article/<int:pk>/add_comment/',AddCommentView.as_view(), name="add-comment"),
    path('weather',get_weather,name="weather"),
    path('result',get_result,name="result"),

    

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
