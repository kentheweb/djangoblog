from django.urls import path
from . import views
from .views import createPost, ViewPosts, EachPost, UpdatePost

urlpatterns = [
     path('', ViewPosts.as_view(), name='home-route'),
     path('about/', views.about, name='about-route'),
     path('each/post/<int:pk>/', EachPost.as_view(), name='each'),
     path('update/post/<int:pk>/', UpdatePost.as_view(), name='update'),
     path('createpost/', createPost.as_view(), name='add-route'),
]
